from django.contrib import admin
from .models import Classes, Profile, Tutor, Student, tutorClasses, Request


# Register your models here.

@admin.register(Profile)
class AdminClasses(admin.ModelAdmin):
    model = Profile
@admin.register(Classes)
class AdminClasses(admin.ModelAdmin):
    model = Classes

@admin.register(Tutor)
class AdminClasses(admin.ModelAdmin):
    model = Tutor

@admin.register(Student)
class AdminClasses(admin.ModelAdmin):
    model = Student

@admin.register(tutorClasses)
class AdminClasses(admin.ModelAdmin):
    model = tutorClasses

@admin.register(Request)
class AdminClasses(admin.ModelAdmin):
    model = Request
#
# @admin.register(TutorClasses)
# class AdminClasses(admin.ModelAdmin):
#     model = TutorClasses
#
# @admin.register(TutorTime)
# class AdminClasses(admin.ModelAdmin):
#     model = TutorTime
# @admin.register(SessionBooked)
# class AdminClasses(admin.ModelAdmin):
#         model = SessionBooked

