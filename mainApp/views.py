import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Classes, Student, Profile, Profile2
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ProfileForm2, TutorForm


# Create your views here.


def login(request):
    return render(request, 'mainApp/login.html')


@login_required
def home(request):
    if request.user.is_authenticated:
        try:
            request.user.profile
        except:  # if a profile does not already exist for the user we will refer them to this form which will force them to update the database
            return redirect('accountSettings')
    user = request.user
    profile = (Profile.objects.filter(user=user).all()[:1])
    if profile[0].is_tutor:  # we already know that they are a tutor!
        return redirect('tutor')
    else:
        return redirect('student')  # we already know that they are a student
    return render(request, 'mainApp/home.html')


def tutorsetting(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    tutor = get_object_or_404(Profile2, user=user)
    tutorform = TutorForm
    if request.method == 'POST':
        if 'edit_profile' in request.POST:
            profileform2 = ProfileForm2(request.POST, instance=profile)
            if profileform2.is_valid():
                profileform2.save()
        if 'edit_tutor' in request.POST:
            tutorform = tutorform(request.POST, instance=tutor)
            if tutorform.is_valid():
                tutor.save()
    context = {
        'form': ProfileForm2,
        'form2': TutorForm,
    }
    return render(request, 'mainApp/tutorSettings.html', context=context)


def tutor(request):
    return render(request, 'mainApp/tutor.html')


def student(request):
    return render(request, 'mainApp/student.html')


@login_required
def accountSettings(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            if profile.is_tutor:
                return redirect('accountSettings2t')
            else:
                return redirect('student')
    form = ProfileForm()
    return render(request, 'mainApp/accountSettings.html', {"form": form})

def accountSettings2t(request): #the next page that a tutor sees when they first log in!
    if request.method == "POST":
        form = TutorForm(request.POST)
        if form.is_valid():
            tutor = form.save(commit=False)
            tutor.user = request.user
            tutor.save()
            return redirect('tutor')
    form = TutorForm()
    return render(request, 'mainApp/accountSettings2t.html', {"form": form})
def classes(request):
    model = Classes
    url = 'https://api.devhub.virginia.edu/v1/courses'
    response = requests.get(url)
    data = response.json()
    courses = data["class_schedules"]["records"]
    AllClasses = {}
    for i in courses:
        Classes.objects.create(subject=i[0], catalogNumber=i[1], classSection=i[2], classNumber=i[3], className=i[4],
                               instructor=i[6]
                               ).save()

    AllClasses = Classes.objects.all().order_by('-classID')
    # https://dev.to/yahaya_hk/how-to-populate-your-database-with-data-from-an-external-api-in-django-398i

    return render(request, 'mainApp/classes.html',
                  {"AllClasses": AllClasses}
                  )
