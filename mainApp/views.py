import requests
from django.shortcuts import render
from mainApp.models import Classes
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    return render(request, 'mainApp/login.html')


@login_required
def home(request):
    return render(request, 'mainApp/home.html')


def classes(request):
    model = Classes
    url = 'https://api.devhub.virginia.edu/v1/courses'
    response = requests.get(url)
    data = response.json()
    courses = data["class_schedules"]["records"]
    i = courses[0]
    AllClasses = {}
    for i in courses:
        Classes.objects.create(subject=i[0],catalogNumber=i[1],classSection=i[2],classNumber=i[3],className=i[4],instructor=i[6]
        ).save()

    AllClasses = Classes.objects.all().order_by('-classID')
    # https://dev.to/yahaya_hk/how-to-populate-your-database-with-data-from-an-external-api-in-django-398i

    return render(request, 'mainApp/classes.html', 
    {"AllClasses": AllClasses}
    )
