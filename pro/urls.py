from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('pro/', views.pro, name='pro'),
    path('thanks/', views.thanks, name='thanks'),
]