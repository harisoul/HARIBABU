from django.contrib import admin
from django.template.context_processors import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.log, name='login'),
    path('home/login/', views.log, name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/',views.home,name='home'),
    path('home/about/', views.about, name='about'),
    path('home/profile/', views.profile, name='profile'),
    path('home/pic/', views.postss, name='posts'),
    path('home/settings/', views.settings, name='settings'),
]