from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


# Create your views here.

# def index(request):
#     return HttpResponse('Hello, World!')


def homeview(request):
    return render(request, 'homepage/homepage.html')