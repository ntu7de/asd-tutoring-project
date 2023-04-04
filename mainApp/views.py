import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Classes, Profile, Tutor, Student, tutorClasses
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ProfileForm2, TutorForm, StudentForm, FirstStudentForm, FirstTutorForm, SearchForm
from django.contrib import messages
from django.db.models import Q

# Create your views here.


def login(request):
    return render(request, 'mainApp/login.html')


@login_required
def home(request):
    if request.user.is_authenticated:  # if the google login works
        try:
            request.user.profile  # see if a profile exists for that user
        except:  # if a profile does not already exist for the user they go to account settings
            return redirect('accountSettings')
    user = request.user
    profile = (Profile.objects.filter(user=user).all()[:1])
    # if we already know that they are a tutor take them to the tutor home
    if profile[0].tutor_or_student == "Tutor":
        return redirect('tutor')
    else:
        # if we already know that they are a student take them to the student home
        return redirect('student')
    return render(request, 'mainApp/home.html')


def tutorsetting(request):  # the account settings page for tutors
    user = request.user  # using this to access the profile of the user logged in
    # profile of the user logged in
    profile = get_object_or_404(Profile, user=user)
    # tutor info of the user logged in
    tutor = get_object_or_404(Tutor, user=user)
    tutorform = TutorForm  # the form that allows them to update their tutor information

    # the field information that is currently in the database for tutor and profile
    monday_start = tutor.monday_start
    monday_end = tutor.monday_end
    tuesday_start = tutor.tuesday_start
    tuesday_end = tutor.tuesday_end
    wednesday_start = tutor.wednesday_start
    wednesday_end = tutor.wednesday_end
    thursday_start = tutor.thursday_start
    thursday_end = tutor.thursday_end
    friday_start = tutor.friday_start
    friday_end = tutor.friday_end
    # if(monday_start == None and monday_end == None  and tuesday_start == None and tuesday_end == None and wednesday_start == None and wednesday_end == None and thursday_start == None and thursday_end == None and friday_start == None and friday_end == None):
    #     messages.error(request, 'Please enter your availability')
    # if (monday_start == None and monday_end != None):
    #     messages.error(request, 'Please enter a start time for Monday')
    # if (monday_start != None and monday_end == None):
    #     messages.error(request, 'Please enter an end time for Monday')
    # if (tuesday_start == None and tuesday_end != None):
    #     messages.error(request, 'Please enter a start time for Tuesday')

    # if (monday_start > monday_end):
    #     messages.error(request, 'Monday start time cannot be after Monday end time')
    # if (tuesday_start > tuesday_end):
    #     messages.error(request, 'Tuesday start time cannot be after Tuesday end time')
    # if (wednesday_start > wednesday_end):
    #     messages.error(request, 'Wednesday start time cannot be after Wednesday end time')
    # if (thursday_start > thursday_end):
    #     messages.error(request, 'Thursday start time cannot be after Thursday end time')
    # if (friday_start > friday_end):
    #     messages.error(request, 'Friday start time cannot be after Friday end time')

    hourly_rate = tutor.hourly_rate
    # if len(hourly_rate) > 5:
    #     messages.error(request, 'Hourly rate cannot be more than 4 digits')

    first_name = profile.first_name
    last_name = profile.last_name
    year = profile.year
    email = profile.email
    pronouns = profile.pronouns
    major = profile.major
    fun_fact = profile.fun_fact

    if request.method == 'POST':
        if 'edit_profile' in request.POST:  # if they're workin with the PROFILE FORM
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
        if 'edit_tutor' in request.POST:  # if they're working with the TUTOR FORM

            tutorform = tutorform(request.POST, instance=tutor)
            if tutorform.is_valid():

                # these if statements exist so that if the fields aren't directly updated they stay the same
                if not tutorform.data['hourly_rate']:
                    tutor.hourly_rate = hourly_rate
                if not tutorform.data['monday_start']:
                    tutor.monday_start = monday_start
                if not tutorform.data['monday_end']:
                    tutor.monday_end = monday_end
                if not tutorform.data['tuesday_start']:
                    tutor.tuesday_start = tuesday_start
                if not tutorform.data['tuesday_end']:
                    tutor.tuesday_end = tuesday_end
                if not tutorform.data['wednesday_start']:
                    tutor.wednesday_start = wednesday_start
                if not tutorform.data['wednesday_end']:
                    tutor.wednesday_end = wednesday_end
                if not tutorform.data['thursday_start']:
                    tutor.thursday_start = thursday_start
                if not tutorform.data['thursday_end']:
                    tutor.thursday_end = thursday_end
                if not tutorform.data['friday_start']:
                    tutor.friday_start = friday_start
                if not tutorform.data['friday_end']:
                    tutor.friday_end = friday_end
                # if not tutorform.data['monday_hours']:
                #     tutor.monday_hours = monday_hours
                # if not tutorform.data['tuesday_hours']:
                #     tutor.tuesday_hours = tuesday_hours
                # if not tutorform.data['wednesday_hours']:
                #     tutor.wednesday_hours = wednesday_hours
                # if not tutorform.data['thursday_hours']:
                #     tutor.thursday_hours = thursday_hours
                # if not tutorform.data['friday_hours']:
                #     tutor.friday_hours = friday_hours
                tutor.save()
    context = {
        'form': ProfileForm2,
        'form2': TutorForm,
    }
    return render(request, 'mainApp/tutorSettings.html', context=context)

def studentsetting(request): #the account settings page for students
    user = request.user #using this to access the profile of the user logged in
    profile = get_object_or_404(Profile, user=user) #profile of the user logged in

    # the field information that is currently in the database for student and profile
    first_name = profile.first_name
    last_name = profile.last_name
    year = profile.year
    email = profile.email
    pronouns = profile.pronouns
    major = profile.major
    fun_fact = profile.fun_fact

    if request.method == 'POST':  # if they're workin with the PROFILE FORM
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
    context = {
        'form': ProfileForm2,
    }
    return render(request, 'mainApp/studentSettings.html', context=context)


def tutor(request):  # tutor home page
    return render(request, 'mainApp/tutor.html')


def student(request):  # student home page
    return render(request, 'mainApp/student.html')


@login_required
# the first form that someone sees when they first log in (account settings)
def accountSettings(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():  # form isn't valid right now
            profile = form.save(commit=False)
            # makes it so that the google auth user is connected to this profile
            profile.user = request.user
            profile.save()
            if profile.tutor_or_student == "Tutor":  # sends you to initially filling in your tutor settings
                return redirect('accountSettings2t')
            else: #sends you to initially filling in your student settings
                stud = Student.objects.create(user=request.user, classes="") #creates an instance of a student
                stud.save() #saves that instance
                return redirect('student')
        else:
            return redirect('accountSettings2s')
    form = ProfileForm()
    return render(request, 'mainApp/accountSettings.html', {"form": form})


def searchClasses(request):
    all_classes = {}
    courseNumber = ''
    if 'name' in request.GET:
        input = request.GET['name'].split(' ')
        inputLength = len(input)

        subject = request.GET['name'].split(' ')[0].upper()
        if inputLength < 0:
            # try:
            courseNumber = request.GET['name'].split(' ')[1]
            # except IndexError:
            #     # messages.add_message(request, messages.WARNING, 'Incorrect Form')
            #     pass
        else:
            # url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01'
            url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1232'

            if inputLength == 1:
                url += '&class_nbr=' + subject
            if inputLength == 2:
                courseNumber = request.GET['name'].split(' ')[1]
                url += '&subject=' + subject + '&catalog_nbr=' + courseNumber
            if inputLength == 3:
                url += '&keyword=' + request.GET['name']
            response = requests.get(url)
            data = response.json()
            name = ''
            classNumber = ''
            a = 0
            for c in data:
                if (a == 0):
                    a += 1
                    name = c['descr']
                    classNumber = c['class_nbr']
                    class_data = Classes(
                        subject=c['subject'],
                        catalognumber=c['catalog_nbr'],
                        classsection=c['class_section'],
                        classnumber=c['class_nbr'],
                        classname=c['descr'],
                        body=c['subject']+' ' +c['catalog_nbr']+' '+c['descr'],
                    )
                    # print(class_data.body)
                class_data.save()

            all_classes = Classes.objects.all()
            if len(data) == 0:
                messages.add_message(
                    request, messages.WARNING, 'No classes found')
            else:
                tutuor_class_data = tutorClasses(
                    classes_id=classNumber,
                    tutor_id=request.user.id,
                )
                tutuor_class_data.save()
                messages.add_message(request, messages.INFO,
                                     name + ' added successfully')
    return render(request, 'mainApp/classsearch.html', {'AllClasses': all_classes})


def detail(request, classnumber):
    model = Classes
    classInfo = Classes.objects.filter(Q(classnumber__icontains=classnumber))
    tutorInfo = tutorClasses.objects.filter(Q(classes__classnumber__icontains=classnumber))
    # ^^Trying to get all the tutor ids related to the selected class; This works
    # Trying to use those ids to obtain the tutor object to use other info like name, rate etc.; This doesn't work because after I get the object a, I can't access fields like first_name etc.
    tutors0=[]
    for i in tutorInfo:
        profile = get_object_or_404(Profile, user=i.tutor)
        tutor = get_object_or_404(Tutor, user= i.tutor)
        # tutors0.append([tutor,profile])
        tutors0.append((profile,tutor))
        # print(tutor.hourly_rate)
    # print(tutors0)
    # for i in tutors0:
    #     print(i)
    #     print(i[1].hourly_rate)
    return render(request, 'mainApp/detail.html', {'classinfo': classInfo, 'tutors': tutors0})

def tutordetail(request):
    return render(request,'mainApp/tutordetail.html')

# def searchClasses(request):
#     all_classes = {}
#     url = ' '
#     if 'name' in request.GET:
#         input1 = request.GET['name']
#         input_length = len(input1)
#         # if input_length == 0:
#         #     messages.add_message(request, messages.WARNING, 'Please enter a class name')
#         if input_length == 1:
#             classnnbr = request.GET['name'].split(' ')[0].upper()
#             url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1238&page=1' + '&class_nbr=' + classnnbr
#         elif input_length == 2:
#             subject = request.GET['name'].split(' ')[0].upper()
#             courseNumber = request.GET['name'].split(' ')[1]
#             url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1238&page=1' + '&subject=' + subject  + '&catalog_nbr=' + courseNumber
#         elif input_length > 2:
#             url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1238&page=1' + '&keyword=' + input1
#         else:
#             messages.add_message(request, messages.WARNING, 'Please enter a class name')
#         response = requests.get(url)
#         data = response.json()
#         for c in data:
#                 name = c['descr']
#                 classNumber = c['class_nbr']
#                 class_data = Classes(
#                     # user=request.user,
#                     subject=c['subject'],
#                     catalognumber=c['catalog_nbr'],
#                     classsection=c['class_section'],
#                     classnumber=c['class_nbr'],
#                     classname=c['descr'],
#                 )
#                 class_data.save()
#                 all_classes = Classes.objects.all()
#         if len(data) == 0:
#                 messages.error(request, 'No classes found')
#
#         else:
#                 # messages.add_message(request, messages.INFO, 'Class ' + name + ' added successfully')
#                 messages.success(request, 'Class ' + name + ' added successfully')
#                 tutuor_class_data = tutorClasses(
#                 classes_id=classNumber,
#                 tutor_id=request.user.id,
#                 )
#                 tutuor_class_data.save()
#
#     return render(request, 'mainApp/classsearch.html', {'AllClasses': all_classes})
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

def StudentSearch(request):
    model = Classes
    data = Classes.objects.all()
    q = request.GET.get('search')
    if q:
        classes = Classes.objects.filter(
            Q(body__icontains=q) | Q(subject__icontains=q) | Q(classname__icontains=q) | Q(catalognumber__icontains=q)
                                         )
        return render(request, 'mainApp/classList.html', {'info': classes})
    else:
        return render(request, 'mainApp/classList.html', {'info': data})



# the tutor settings that a tutor sees when they first log in (right after initial account settings)
def accountSettings2t(request):
    if request.method == "POST":
        # the tutor form that requires you to add everything
        form = FirstTutorForm(request.POST)
        if form.is_valid():
            tutor = form.save(commit=False)
            tutor.user = request.user  # connects the tutor to the user
            tutor.save()
            return redirect('classes')  # send them to the classes page
    form = FirstTutorForm()
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


def accountDisplay(request):
    user = request.user #using this to access the profile of the user logged in
    profile = get_object_or_404(Profile, user=user) #profile of the user logged in
    return render(request, 'mainApp/accountDisplay.html', {"profile": profile})
