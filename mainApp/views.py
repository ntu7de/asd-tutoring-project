import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Classes, Profile, Tutor, Student
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ProfileForm2, TutorForm, StudentForm, FirstStudentForm, FirstTutorForm
from django.contrib import messages
from django.db.models import Q

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
    if profile[0].tutor_or_student == "Tutor":  # if we already know that they are a tutor take them to the tutor home
        return redirect('tutor')
    else:
        return redirect('student')   # if we already know that they are a student take them to the student home
    return render(request, 'mainApp/home.html')


def tutorsetting(request): #the account settings page for tutors
    user = request.user #using this to access the profile of the user logged in
    profile = get_object_or_404(Profile, user=user) #profile of the user logged in
    tutor = get_object_or_404(Tutor, user=user) #tutor info of the user logged in
    tutorform = TutorForm #the form that allows them to update their tutor information

    # the field information that is currently in the database for tutor and profile
    monday_hours = tutor.monday_hours
    tuesday_hours = tutor.tuesday_hours
    wednesday_hours = tutor.wednesday_hours
    thursday_hours = tutor.thursday_hours
    friday_hours = tutor.friday_hours
    hourly_rate = tutor.hourly_rate
    first_name = profile.first_name
    last_name = profile.last_name
    year = profile.year
    email = profile.email
    pronouns = profile.pronouns
    major = profile.major
    fun_fact = profile.fun_fact

    if request.method == 'POST':
        if 'edit_profile' in request.POST: #if they're workin with the PROFILE FORM
            profileform2 = ProfileForm2(request.POST, instance=profile)
            if profileform2.is_valid():

                # all of these if statements exist so that if the fields aren't directly updated they stay the same
                if not profileform2.data['first_name']:
                    profile.first_name = first_name
                if not profileform2.data['last_name']:
                    profile.last_name = last_name
                if not profileform2.data['year']:
                    profile.year = year
                if not profileform2.data['email']:
                    profile.email = email
                if not profileform2.data['pronouns']:
                    profile.pronouns = pronouns
                if not profileform2.data['major']:
                    profile.major = major
                if not profileform2.data['fun_fact']:
                    profile.fun_fact = fun_fact

                profileform2.save()
        if 'edit_tutor' in request.POST: #if they're working with the TUTOR FORM

            tutorform = tutorform(request.POST, instance=tutor)
            if tutorform.is_valid():

                # these if statements exist so that if the fields aren't directly updated they stay the same
                if not tutorform.data['hourly_rate']:
                    tutor.hourly_rate = hourly_rate
                if not tutorform.data['monday_hours']:
                    tutor.monday_hours = monday_hours
                if not tutorform.data['tuesday_hours']:
                    tutor.tuesday_hours = tuesday_hours
                if not tutorform.data['wednesday_hours']:
                    tutor.wednesday_hours = wednesday_hours
                if not tutorform.data['thursday_hours']:
                    tutor.thursday_hours = thursday_hours
                if not tutorform.data['friday_hours']:
                    tutor.friday_hours = friday_hours
                tutor.save()
    context = {
        'form': ProfileForm2,
        'form2': TutorForm,
    }
    return render(request, 'mainApp/tutorSettings.html', context=context)

def studentsetting(request): #the account settings page for students
    user = request.user #using this to access the profile of the user logged in
    profile = get_object_or_404(Profile, user=user) #profile of the user logged in
    student = get_object_or_404(Student, user=user) #student info of the user logged in
    studentform = StudentForm #the form that allows them to update their student information

    # the field information that is currently in the database for student and profile
    classes = student.classes
    first_name = profile.first_name
    last_name = profile.last_name
    year = profile.year
    email = profile.email
    pronouns = profile.pronouns
    major = profile.major
    fun_fact = profile.fun_fact

    if request.method == 'POST': #if they're workin with the PROFILE FORM
        if 'edit_profile' in request.POST:
            profileform2 = ProfileForm2(request.POST, instance=profile)
            if profileform2.is_valid():

                # all of these if statements exist so that if the fields aren't directly updated they stay the same
                if not profileform2.data['first_name']:
                    profile.first_name = first_name
                if not profileform2.data['last_name']:
                    profile.last_name = last_name
                if not profileform2.data['year']:
                    profile.year = year
                if not profileform2.data['email']:
                    profile.email = email
                if not profileform2.data['pronouns']:
                    profile.pronouns = pronouns
                if not profileform2.data['major']:
                    profile.major = major
                if not profileform2.data['fun_fact']:
                    profile.fun_fact = fun_fact

                profileform2.save()
        if 'edit_student' in request.POST: #if they're working with the STUDENT FORM
            studentform = studentform(request.POST, instance=student)
            if studentform.is_valid():
                # this is here so we keep it as the stuff that is already in the database if it's not updated
                if not studentform.data['classes']:
                    student.classes = classes

                student.save()
    context = {
        'form': ProfileForm2,
        'form2': StudentForm,
    }
    return render(request, 'mainApp/studentSettings.html', context=context)


def tutor(request): #tutor home page
    return render(request, 'mainApp/tutor.html')


def student(request): #student home page
    return render(request, 'mainApp/student.html')


@login_required
def accountSettings(request): #the first form that someone sees when they first log in (account settings)
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid(): #form isn't valid right now
            profile = form.save(commit=False)
            profile.user = request.user #makes it so that the google auth user is connected to this profile
            profile.save()
            if profile.tutor_or_student == "Tutor": #sends you to initially filling in your tutor settings
                return redirect('accountSettings2t')
            else: #sends you to initially filling in your student settings
                return redirect('accountSettings2s')
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

def StudentSearch(request):
    model = Classes
    data = Classes.objects.all()
    context_dict = {
        'info': data
    }
    q = request.GET.get('search')
    if q:
        classes = Classes.objects.filter(Q(subject__icontains=q) | Q(classname__icontains=q) |  Q(catalognumber__icontains=q) 
                                         )
        return render(request,'mainApp/classList.html',{'info':classes})
    else:
        return render(request,'mainApp/classList.html',context_dict)



def accountSettings2s(request): #the student settings that a student sees when they first log in (right after initial account settings)
    if request.method == "POST":
        form = FirstStudentForm(request.POST) #the student form that requires you to add everything
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user #connects the student to the user
            student.save()
            return redirect('student') #send them to the student home page
    form = FirstStudentForm()
    return render(request, 'mainApp/accountSettings2s.html', {"form": form})



def accountSettings2t(request): #the tutor settings that a tutor sees when they first log in (right after initial account settings)
    if request.method == "POST":
        form = FirstTutorForm(request.POST) #the tutor form that requires you to add everything
        if form.is_valid():
            tutor = form.save(commit=False)
            tutor.user = request.user #connects the tutor to the user
            tutor.save()
            return redirect('classes') #send them to the classes page
    form = FirstTutorForm()
    return render(request, 'mainApp/accountSettings2t.html', {"form": form})


def accountDisplay(request): # display account settings for tutors/students
    user = request.user #using this to access the profile of the user logged in
    profile = get_object_or_404(Profile, user=user) #profile of the user logged in
    return render(request, 'mainApp/accountDisplay.html', {"profile": profile})



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
