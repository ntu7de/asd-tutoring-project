import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Classes, Profile, Tutor, Student
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ProfileForm2, TutorForm, StudentForm


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
    tutor = get_object_or_404(Tutor, user=user)
    tutorform = TutorForm
    classes = tutor.classes
    hourly_rate = tutor.hourly_rate
    first_name = profile.first_name
    last_name = profile.last_name
    year = profile.year
    email = profile.email
    pronouns = profile.pronouns
    major = profile.major
    fun_fact = profile.fun_fact
    if request.method == 'POST':
        if 'edit_profile' in request.POST:
            profileform2 = ProfileForm2(request.POST, instance=profile)
            if profileform2.is_valid():
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
        if 'edit_tutor' in request.POST:
            tutorform = tutorform(request.POST, instance=tutor)
            if tutorform.is_valid():
                if not tutorform.data['classes']:
                    tutor.classes = classes
                if not tutorform.data['hourly_rate']:
                    tutor.hourly_rate = hourly_rate
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
    classes = student.classes
    first_name = profile.first_name
    last_name = profile.last_name
    year = profile.year
    email = profile.email
    pronouns = profile.pronouns
    major = profile.major
    fun_fact = profile.fun_fact
    if request.method == 'POST':
        if 'edit_profile' in request.POST:
            profileform2 = ProfileForm2(request.POST, instance=profile)
            if profileform2.is_valid():
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
        if 'edit_student' in request.POST:
            studentform = studentform(request.POST, instance=student)
            if studentform.is_valid():
                if not studentform.data['classes']:
                    student.classes = classes
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

def searchClasses(request):
    all_classes = {}
    if 'name' in request.GET:
        # name = request.GET['class']
        subject = request.GET['name'].split(' ')[0]
        courseNumber = request.GET['name'].split(' ')[1]
        url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1238&page=1' + '&subject=' + subject + '&catalog_nbr=' + courseNumber
        response = requests.get(url)
        data = response.json()
        # classes = data['class']
        for c in data:
            class_data = Classes(
                subject=c['subject'],
                catalogNumber=c['catalog_nbr'],
                classSection=c['class_section'],
                classNumber=c['class_nbr'],
                className=c['descr'],
            )
            class_data.save()
            all_classes = Classes.objects.all()
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
