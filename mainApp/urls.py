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
    # path('accountSettings2s/', views.accountSettings2s, name='accountSettings2s'),
    path("", views.home, name='home'),
    path('tutor/', views.tutor, name = 'tutor'),
    path('tutorsetting/', views.tutorsetting, name = 'tutorsetting'),
    path('studentsetting/', views.studentsetting, name = 'studentsetting'),
    path('student/', views.student, name = 'student'),
    path('classes/', views.searchClasses, name = 'classes'),
    path('classList/', views.StudentSearch, name = 'classList'),
    path('classList/<int:classnumber>/', views.detail, name='detail'),
    path('classList/tutordetail/<int:profileid>/',views.tutordetail,name='tutordetail'),
    path('accountDisplay/', views.accountDisplay, name='accountDisplay'),

    path('classes/<int:classnumber>/', views.classesdetail, name = 'classesdetail'),

    path('accountDisplayStudent/', views.accountDisplayStudent, name='accountDisplay'),
    path('tutorCalendar/', views.CalendarView.as_view(), name='tutorCalendar'),
]

