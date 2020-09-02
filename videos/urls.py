from django.urls import path

from .views import VideoListView, VideoDetailView, LessonDetailView

app_name = 'videos'

urlpatterns = [
    path('', VideoListView.as_view(), name='list'),
    path('<slug>', VideoDetailView.as_view(), name='detail'),
    path('<video_slug>/<lesson_slug>', LessonDetailView.as_view(), name='lesson-detail')
]
