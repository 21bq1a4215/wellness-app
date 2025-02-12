from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Course


class CoursePermissionMixin:
    """
    This function will attemp to give permision
    to content to only user subscribe 
    """
    def dispatch(self, request, *args, **kwargs):
        course = get_object_or_404(Course, slug=self.kwargs["slug"])
        subscription = request.user.subscription
        pricing_tier = subscription.pricing
        if not pricing_tier in course.pricing_tiers.all():
            messages.info(request, "You do not have access to this course")
            return redirect("videos:course-list")
        return super().dispatch(request, *args, **kwargs)
