import requests
from django.shortcuts import render, redirect
from .models import Classes, Student
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
# Create your views here.


def login(request):
    return render(request, 'mainApp/login.html')


@login_required
def home(request):
    if request.user.is_authenticated:
        try:
            request.user.profile
        except: #if a profile does not already exist for the user we will refer them to this form which will force them to update the database
            return redirect('accountSettings')

    return render(request,'mainApp/home.html')

def tutor(request):
    return render(request, 'mainApp/tutor.html')

def student(request):
    return render(request, 'mainApp/student.html')
@login_required
def accountSettings(request):
    theEmail = request.user.email
    user = Student.objects.filter(email=theEmail).values()
    context = {
        'user': user
    }
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('home')
    form = ProfileForm()
    return render(request, 'mainApp/accountSettings.html', {"form": form})

def classes(request):
    model = Classes
    url = 'https://api.devhub.virginia.edu/v1/courses'
    response = requests.get(url)
    data = response.json()
    courses = data["class_schedules"]["records"]
    AllClasses = {}
    for i in courses:
        Classes.objects.create(subject=i[0],catalogNumber=i[1],classSection=i[2],classNumber=i[3],className=i[4],instructor=i[6]
        ).save()

    AllClasses = Classes.objects.all().order_by('-classID')
    # https://dev.to/yahaya_hk/how-to-populate-your-database-with-data-from-an-external-api-in-django-398i

    return render(request, 'mainApp/classes.html', 
    {"AllClasses": AllClasses}
    )
