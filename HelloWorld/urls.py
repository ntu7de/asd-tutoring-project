from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeview, name='homepage')
]

# path('', views.index, name="homepage")