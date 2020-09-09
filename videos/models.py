from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from allauth.account.signals import email_confirmed

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

User = get_user_model()


class Pricing(models.Model):
    """
    Model sets the price parameters of the video course
    """
    name = models.CharField(max_length=100, null=True, blank=True)  # Basic / Pro
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    """
    Model for subcriptions to manage each
    user subcription and permisions
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE, related_name='subscriptions')
    created = models.DateTimeField(auto_now_add=True)
    stripe_subscription_id = models.CharField(max_length=50)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email



class Course(models.Model):
    """
    Model to manage and add the courses
    """
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to="thumbnails/")
    description = models.TextField()

    def __str__(self):
        return self.name

    
    def get_absolute_url(self):
        return reverse("videos:course-detail", kwargs={"slug": self.slug})


class Video(models.Model):
    """
    Model for manageing and adding videos
    using vimeo, can add videos using vimeo id
    on the vimeo dashboard will generate the vimeo id needed
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    vimeo_id = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ["order"] 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("videos:video-detail", kwargs={
            "video_slug": self.slug,
            "slug": self.course.slug
        })


def pre_save_course(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


def pre_save_video(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


def post_save_user(sender, instance, created, *args, **kwargs):
    if created:
        free_trial_pricing = Pricing.objects.get(name='Free Trial')
        subscription = Subscription.objects.create(
            user=instance, 
            pricing=free_trial_pricing
        )
        stripe_customer = stripe.Customer.create(
            email=instance.email
        )
        stripe_subscription = stripe.Subscription.create(
            customer=stripe_customer['id'],
            items=[{'price': 'price_1HMtRnHeew9pZh4QRDKWiRKq'}]
        )
        print(stripe_subscription)
        subscription.status = stripe_subscription["status"] # trialing
        subscription.stripe_subscription_id = stripe_subscription["id"]
        subscription.save()


post_save.connect(post_save_user, sender=User)
pre_save.connect(pre_save_course, sender=Course)
pre_save.connect(pre_save_video, sender=Video)
