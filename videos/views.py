from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Course, Video


class CourseListView(generic.ListView):
    """
    Loads the course list from the db
    """
    template_name = "videos/course_list.html"
    queryset = Course.objects.all()


class CourseDetailView(generic.DetailView):
    """
    Loads each course detail info
    """
    template_name = "videos/course_detail.html"
    queryset = Course.objects.all()


class VideoDetailView(LoginRequiredMixin, generic.DetailView):
    """
    This function will display the video course
    for users subscribed
    """
    template_name = "videos/video_detail.html"

    def get_context_data(self, **kwargs):
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        course = self.get_course()
        subscription = self.request.user
        context.update({
            "has_permission": subscription
        })
        return context

    def get_course(self):
        return get_object_or_404(Course, slug=self.kwargs["slug"])

    def get_object(self):
        video = get_object_or_404(Video, slug=self.kwargs["video_slug"])
        return video

    def get_queryset(self):
        course = self.get_course()
        return course.videos.all()
