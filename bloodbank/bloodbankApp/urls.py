from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path(r'', views.index, name='home'),
    #path(r'login/', views.login, name='login'),
    path(r'donorsignup/', views.donorSign, name='donorSignUp'),
    path(r'volunteersignup/', views.volunteer, name='volunteer'),
    path(r'table/<str:table_name>',views.show_table, name='table'),
    path(r'adddonation/', views.donation, name='donation'),
    path(r'addpatient/', views.patient, name='patient'),
    path(r'update/<str:table_name>/<int:pri_k>', views.update, name='update')
]