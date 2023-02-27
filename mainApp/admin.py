from django.contrib import admin
from .models import Classes, Tutor, Student, TutorClasses, TutorTime, SessionBooked
# Register your models here.
@admin.register(Classes)
class AdminClasses(admin.ModelAdmin):
    model = Classes

@admin.register(Tutor)
class AdminClasses(admin.ModelAdmin):
    model = Tutor

@admin.register(Student)
class AdminClasses(admin.ModelAdmin):
    model = Student

@admin.register(TutorClasses)
class AdminClasses(admin.ModelAdmin):
    model = TutorClasses

@admin.register(TutorTime)
class AdminClasses(admin.ModelAdmin):
    model = TutorTime
@admin.register(SessionBooked)
class AdminClasses(admin.ModelAdmin):
        model = SessionBooked

