from django.urls import path
from . import views

urlpatterns = [
    path('pro/', views.pro, name='pro'),
    path('thanks/', views.thanks, name='thanks'),
    path('pro-members/', views.pro_members, name='pro-members'),
]