from django.contrib import admin
from django.urls import path
from task1 import views  

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
