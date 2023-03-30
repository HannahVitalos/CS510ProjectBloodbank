from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    #path(r'login/', views.login, name='login'),
    #path(r'donorsignup/', views.donorSign, name='donorSignUp'),
    #path(r'volunteer/', views.volunteer, name='volunteer'),
]