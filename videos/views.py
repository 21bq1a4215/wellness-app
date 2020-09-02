from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from pro.models import UserMembership
from .models import Video, Lesson


class VideoListView(ListView):
    model = Video


class VideoDetailView(DetailView):
    model = Video

class LessonDetailView(LoginRequiredMixin, View):

    def get(self, request, video_slug, lesson_slug, *args, **kwargs):
        video = get_object_or_404(Video, slug=video_slug)
        lesson = get_object_or_404(Lesson, slug=lesson_slug)
        user_membership = get_object_or_404(UserMembership, user=request.user)
        user_membership_type = user_membership.membership.membership_type
        video_allowed_mem_types = video.allowed_memberships.all()
        context = { 'object': None }
        if video_allowed_mem_types.filter(membership_type=user_membership_type).exists():
            context = {'object': lesson}
        return render(request, "videos/lesson_detail.html", context)