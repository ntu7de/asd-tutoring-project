from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required


# Create your views here.

# def index(request):
#     return HttpResponse('Hello, World!')


def homeview(request):
    return render(request, 'homepage/homepage.html')

@login_required
def home(request):
    return render(request, 'mainApp/home.html')
