from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('accountSettings/', views.accountSettings, name='accountSettings'),
    path('accountSettings2t/', views.accountSettings2t, name='accountSettings2t'),
    path("", views.home, name='home'),
    path('tutor/', views.tutor, name = 'tutor'),
    path('tutorsetting/', views.tutorsetting, name = 'tutorsetting'),
    path('student/', views.student, name = 'student'),
    path('classes/', views.classes, name = 'classes'),
]