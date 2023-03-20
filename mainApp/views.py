import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Classes, Profile, Tutor, Student
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ProfileForm2, TutorForm, StudentForm, FirstStudentForm, FirstTutorForm
from django.contrib import messages


# Create your views here.


def login(request):
    return render(request, 'mainApp/login.html')


@login_required
def home(request):
    if request.user.is_authenticated: #if the google login works
        try:
            request.user.profile #see if a profile exists for that user
        except: # if a profile does not already exist for the user they go to account settings
            return redirect('accountSettings')
    user = request.user
    profile = (Profile.objects.filter(user=user).all()[:1])
    if profile[0].is_tutor:  # if we already know that they are a tutor take them to the tutor home
        return redirect('tutor')
    else:
        return redirect('student')   # if we already know that they are a student take them to the student home
    return render(request, 'mainApp/home.html')


def tutorsetting(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    tutor = get_object_or_404(Tutor, user=user)
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

def studentsetting(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    student = get_object_or_404(Student, user=user)
    studentform = StudentForm
    if request.method == 'POST':
        if 'edit_profile' in request.POST:
            profileform2 = ProfileForm2(request.POST, instance=profile)
            if profileform2.is_valid():
                profileform2.save()
        if 'edit_student' in request.POST:
            studentform = studentform(request.POST, instance=student)
            if studentform.is_valid():
                student.save()
    context = {
        'form': ProfileForm2,
        'form2': StudentForm,
    }
    return render(request, 'mainApp/studentSettings.html', context=context)


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
                return redirect('accountSettings2s')
    form = ProfileForm()
    return render(request, 'mainApp/accountSettings.html', {"form": form})

# def searchClasses(request):
#     all_classes = {}
#     if 'name' in request.GET:
#         # name = request.GET['class']
#         subject = request.GET['name'].split(' ')[0]
#         courseNumber = request.GET['name'].split(' ')[1]
#         url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1238&page=1' + '&subject=' + subject + '&catalog_nbr=' + courseNumber
#         response = requests.get(url)
#         data = response.json()
#
#         name = ''
#         for c in data:
#             name = c['descr']
#             # classname = c['descr']
#             class_data = Classes(
#                 user=request.user,
#                 subject=c['subject'],
#                 catalognumber=c['catalog_nbr'],
#                 classsection=c['class_section'],
#                 classnumber=c['class_nbr'],
#                 classname=c['descr'],
#             )
#             class_data.save()
#             all_classes = Classes.objects.filter(user=request.user)
#         if len(data) == 0:
#             messages.add_message(request, messages.WARNING, 'No classes found')
#         else:
#             messages.add_message(request, messages.INFO, 'Class ' + name + ' added successfully')
#
#     return render(request, 'mainApp/classsearch.html', {'AllClasses': all_classes})


def searchClasses(request):
    all_classes = {}
    if 'name' in request.GET:
        subject = request.GET['name'].split(' ')[0]
        try:
            courseNumber = request.GET['name'].split(' ')[1]
        except IndexError:
            messages.add_message(request, messages.WARNING, 'Incorrect Form')
        else:
            url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1238&page=1' + '&subject=' + subject + '&catalog_nbr=' + courseNumber
            response = requests.get(url)
            data = response.json()
            name = ''
            for c in data:
                name = c['descr']
                class_data = Classes(
                    user=request.user,
                    subject=c['subject'],
                    catalognumber=c['catalog_nbr'],
                    classsection=c['class_section'],
                    classnumber=c['class_nbr'],
                    classname=c['descr'],
                )
                class_data.save()
            all_classes = Classes.objects.filter(user=request.user)
            if len(data) == 0:
                messages.add_message(request, messages.WARNING, 'No classes found')
            else:
                messages.add_message(request, messages.INFO, 'Class ' + name + ' added successfully')
    return render(request, 'mainApp/classsearch.html', {'AllClasses': all_classes})


class classList(ListView):
    model = Classes
    template_name = 'mainApp/classList.html'
    context_object_name = 'AllClasses'
    def get_queryset(self):
        return Classes.objects.all()



def accountSettings2s(request): #the next page that a student sees when they first log in!
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('student')
    form = StudentForm()
    return render(request, 'mainApp/accountSettings2s.html', {"form": form})



def accountSettings2t(request): #the next page that a tutor sees when they first log in!
    if request.method == "POST":
        form = TutorForm(request.POST)
        if form.is_valid():
            tutor = form.save(commit=False)
            tutor.user = request.user
            tutor.save()
            return redirect('classes')
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
