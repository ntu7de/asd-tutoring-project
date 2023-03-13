from django.contrib import admin
from .models import Classes, Student,  Profile, Profile2

# Register your models here.

@admin.register(Profile)
class AdminClasses(admin.ModelAdmin):
    model = Profile
@admin.register(Classes)
class AdminClasses(admin.ModelAdmin):
    model = Classes

@admin.register(Profile2)
class AdminClasses(admin.ModelAdmin):
    model = Profile2

@admin.register(Student)
class AdminClasses(admin.ModelAdmin):
    model = Student

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

