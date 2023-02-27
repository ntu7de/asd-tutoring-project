from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    return render(request, 'mainApp/login.html')
@login_required
def home(request):
    return render(request, 'mainApp/home.html')
def tutor(request):
    return render(request, 'mainApp/tutor.html')

def student(request):
    return render(request, 'mainApp/student.html')
@login_required
def accountSettings(request):
    return render(request, 'mainApp/accountSettings.html')
