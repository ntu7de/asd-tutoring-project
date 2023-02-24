from django.contrib import admin
from .models import Classes
# Register your models here.
@admin.register(Classes)
class AdminClasses(admin.ModelAdmin):
    model = Classes