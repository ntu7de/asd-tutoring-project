from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.homeview, name='homepage'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path("", views.home, name='home'),
]
# path('', views.homeview, name="homepage")
# path('', views.index, name="homepage")