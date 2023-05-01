import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.utils.safestring import mark_safe
from django.views import generic

from .models import Classes, Profile, Tutor, Student, tutorClasses, Request
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ProfileForm2, TutorForm, StudentForm, FirstStudentForm, FirstTutorForm, SearchForm, AlertForm
from django.contrib import messages
from django.db.models import Q
import calendar
from datetime import date, datetime
import datetime
from calendar import HTMLCalendar
from .utils import Calendar


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

@login_required
def tutorsetting(request):  # the account settings page for tutors
    u = request.user
    try:  # check if user is accessing wrong side
        temp = get_object_or_404(Tutor, user=u)
    except:
        return redirect('student')
    user = request.user  # using this to access the profile of the user logged in
    profile = get_object_or_404(Profile, user=user)  # profile of the user logged in
    tutor = get_object_or_404(Tutor, user=user)  # tutor info of the user logged in
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

    hourly_rate = tutor.hourly_rate

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
                if profileform2.data['year'] == "Select a Year":
                    profile.year = year
                if not profileform2.data['email']:
                    profile.email = email
                if profileform2.data['pronouns'] == "Select Pronouns":
                    profile.pronouns = pronouns
                if not profileform2.data['major']:
                    profile.major = major
                if not profileform2.data['fun_fact']:
                    profile.fun_fact = fun_fact

                profileform2.save()
        if 'edit_tutor' in request.POST:  # if they're working with the TUTOR FORM
            tutorID = tutor.user
            user_id = request.user
            tutorform = tutorform(request.POST, instance=tutor)
            if tutorform.is_valid():
                if tutorform.is_valid():
                    hourly_rate = tutorform.cleaned_data['hourly_rate']
                    if hourly_rate != None:
                        if hourly_rate < 0 or hourly_rate < 12.5 or hourly_rate > 100:
                            if hourly_rate < 0:
                                # If the hourly rate is negative, show an error message
                                messages.add_message(request, messages.ERROR, 'Hourly rate cannot be negative')
                            if hourly_rate < 12.5:
                                messages.add_message(request, messages.ERROR,
                                                     'Hourly rate cannot be less than minimum wage')
                            if hourly_rate > 100:
                                messages.add_message(request, messages.ERROR, 'Hourly rate cannot be greater than $100')
                    if ((tutorform.data['monday_start'] == "Not Available" and tutorform.data['monday_end'] != "Not Available") or \
                            (tutorform.data['monday_end'] == "Not Available" and tutorform.data['monday_start'] != "Not Available") or \
                            (tutorform.data['tuesday_start'] == "Not Available" and tutorform.data['tuesday_end'] != "Not Available") or \
                            (tutorform.data['tuesday_end'] == "Not Available" and tutorform.data['tuesday_start'] != "Not Available") or \
                            (tutorform.data['wednesday_start'] == "Not Available" and tutorform.data['wednesday_end'] != "Not Available") or \
                            (tutorform.data['wednesday_end'] == "Not Available" and tutorform.data['wednesday_start'] != "Not Available") or \
                            (tutorform.data['thursday_start'] == "Not Available" and tutorform.data['thursday_end'] != "Not Available") or \
                            (tutorform.data['thursday_end'] == "Not Available" and tutorform.data['thursday_start'] != "Not Available") or \
                            (tutorform.data['friday_start'] == "Not Available" and tutorform.data['friday_end'] != "Not Available") or \
                            (tutorform.data['friday_end'] == "Not Available" and tutorform.data['friday_start'] != "Not Available")):
                        messages.add_message(request, messages.WARNING, '"Not Available" must be selected for both start and end')
                    else:
                        if not tutorform.data['hourly_rate']:
                            tutor.hourly_rate = hourly_rate
                        if tutorform.data['monday_start'] == "Select Time":
                            tutor.monday_start = monday_start
                        if tutorform.data['monday_end'] == "Select Time":
                            tutor.monday_end = monday_end
                        if tutorform.data['tuesday_start'] == "Select Time":
                            tutor.tuesday_start = tuesday_start
                        if tutorform.data['tuesday_end'] == "Select Time":
                            tutor.tuesday_end = tuesday_end
                        if tutorform.data['wednesday_start'] == "Select Time":
                            tutor.wednesday_start = wednesday_start
                        if tutorform.data['wednesday_end'] == "Select Time":
                            tutor.wednesday_end = wednesday_end
                        if tutorform.data['thursday_start'] == "Select Time":
                            tutor.thursday_start = thursday_start
                        if tutorform.data['thursday_end'] == "Select Time":
                            tutor.thursday_end = thursday_end
                        if tutorform.data['friday_start'] == "Select Time":
                            tutor.friday_start = friday_start
                        if tutorform.data['friday_end'] == "Select Time":
                            tutor.friday_end = friday_end
                        tutor.save()
                        return redirect('tutor')
    context = {
        'form': ProfileForm2,
        'form2': TutorForm,
    }
    return render(request, 'mainApp/tutorSettings.html', context=context)


def studentsetting(request):  # the account settings page for students
    user = request.user  # using this to access the profile of the user logged in
    try:  # check if user is accessing wrong side
        temp = get_object_or_404(Student, user=user)
    except:
        return redirect('tutor')
    profile = get_object_or_404(Profile, user=user)  # profile of the user logged in

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
                if profileform2.data['year'] == "Select a Year":
                    profile.year = year
                if not profileform2.data['email']:
                    profile.email = email
                if profileform2.data['pronouns'] == "Select Pronouns":
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

@login_required
def tutor(request):  # tutor home page
    u = request.user
    try: #check if user is accessing wrong side
        tutor = get_object_or_404(Tutor, user=u)
    except:
        return redirect('student')
    requests = Request.objects.filter(tutor=tutor) #get all of the requests associated with the tutor
    requestlist = [] #the array that we will put all of the relevant info for each request into
    classes = tutorClasses.objects.filter(tutor=u)
    classlist = []
    for c in classes:
        classname = c.classes.classname
        classlist.append(classname)
    for i in requests:
        #the student first name
        user = i.student
        profile = get_object_or_404(Profile, user=user) #this will get us the tutor's profile
        first_name = profile.first_name
        #the student last name
        last_name = profile.last_name
        d = i.date
        thedate = datetime.datetime.strptime(d, "%Y-%m-%d").date()
        start_time = i.startTime
        end_time = i.endTime
        location = i.location
        approved = i.approved
        if(date.today() <= thedate):
            requestlist.append((first_name, last_name, d, start_time, end_time, location, approved))

    if request.method == 'POST':
        if 'approve' in request.POST:  # approving and denying
            a = request.POST.get('approve', [])
            b = a[1:]
            c = b[:-1]
            d = c.translate({ord("'"): None})
            my_list = d.split(", ")
            # p = get_object_or_404(Profile, first_name=my_list[0], last_name=my_list[1], tutor_or_student="Student") #error fixx
            r = get_object_or_404(Request, tutor=tutor, student=user, date=my_list[2], startTime=my_list[3], endTime=my_list[4])
            r.approved = 'approved'
            r.save()
            return redirect('tutor')
        if 'deny' in request.POST:
            a = request.POST.get('deny', [])
            b = a[1:]
            c = b[:-1]
            d = c.translate({ord("'"): None})
            my_list = d.split(", ")
            p = get_object_or_404(Profile, first_name=my_list[0], last_name=my_list[1])
            r = get_object_or_404(Request, tutor=tutor, student=p.user, date=my_list[2], startTime=my_list[3],
                                  endTime=my_list[4])
            r.approved = 'denied'
            r.save()
            return redirect('tutor')


    return render(request, 'mainApp/tutor.html', {'requestlist': requestlist, 'classlist': classlist})

@login_required
def student(request):  # student home page
    student = request.user
    try: #check if user is accessing wrong side
        temp = get_object_or_404(Student, user=student)
    except:
        return redirect('tutor')
    requests = Request.objects.filter(student=student)#get all of the requests associated with the studen
    requestlist = [] #the array that we will put all of the relevant info for each request into
    for i in requests:
        #the tutor first name
        profile = get_object_or_404(Profile, user=i.tutor.user) #this will get us the tutor's profile
        first_name = profile.first_name
        #the tutor last name
        last_name = profile.last_name
        #the date
        d = i.date
        thedate = datetime.datetime.strptime(d, "%Y-%m-%d").date()
        #the start time
        start_time = i.startTime
        #the end time
        end_time = i.endTime
        #location
        location = i.location
        #status of approvall
        approved = i.approved
        if (date.today() <= thedate):
            requestlist.append((first_name, last_name, d, start_time, end_time, location, approved))
    return render(request, 'mainApp/student.html', {'requestlist': requestlist})


@login_required
# the first form that someone sees when they first log in (account settings)
def accountSettings(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():  # form isn't valid right now
            # if not form.email.to_python(request, value= str).__contains__("@"):
            #     return redirect('login')
            profile = form.save(commit=False)
            # makes it so that the google auth user is connected to this profile
            profile.user = request.user
            profile.save()
            if profile.tutor_or_student == "Tutor":  # sends you to initially filling in your tutor settings
                return redirect('accountSettings2t')
            else:  # sends you to initially filling in your student settings
                stud = Student.objects.create(user=request.user, classes="")  # creates an instance of a student
                stud.save()  # saves that instance
                return redirect('student')
        else:
            messages.add_message(request, messages.WARNING, 'One or more fields are invalid.')
            return redirect('accountSettings')
    form = ProfileForm()
    return render(request, 'mainApp/accountSettings.html', {"form": form})


@login_required
def classesdetail(request, classnumber):
    # https://www.w3schools.com/django/showdjango.php?filename=demo_add_link_details1
    u = request.user
    try:  # check if user is accessing wrong side
        temp = get_object_or_404(Tutor, user=u)
    except:
        return redirect('student')
    currentClass = Classes.objects.get(classnumber = classnumber)
    template = loader.get_template('mainApp/classesdetail.html')
    context = {
        'Classes' : currentClass,
    }
    if request.method == 'POST':
        classes_id = classnumber
        tutor_id = request.user.id
        comment = request.POST.get('comment')
        tutor_class_data = tutorClasses(
            classes_id=classnumber,
            tutor_id=request.user.id,
            comment = comment,
        )
        tutorClass = tutorClasses.objects.filter(classes_id=classes_id, tutor_id=tutor_id)
        # tutorClasses(request.POST, classes_id=classes_id, tutor_id=tutor_id)

        if tutorClass:
            messages.add_message(request, messages.INFO, "Class already added")
        else:
            tutor_class_data.save()
            return redirect('/classes')

    return HttpResponse(template.render(context, request))

@login_required
def searchClasses(request):
    # all_classes = {}
    all_classes = Classes.objects.all()
    classAll = {
        "classes": all_classes
    }
    if 'name' in request.GET:
        input_value = request.GET['name']
        # data = ''
        if input_value.isdigit():
            url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1232'
            url += '&catalog_nbr=' + input_value
            response = requests.get(url)
            data = response.json()
            # messages.add_message(request, messages.INFO,url)
            currentClasses = []
            if len(data) > 1:
                for c in data:
                    name = c['descr']
                    if name in currentClasses:
                        i = 1
                    else:
                        currentClasses.append(name)
                        classNumber = c['class_nbr']
                        catalog_nbr = c['catalog_nbr']
                        subject = c['subject']
                        class_data = Classes(
                            subject=c['subject'],
                            catalognumber=c['catalog_nbr'],
                            classsection=c['class_section'],
                            classnumber=c['class_nbr'],
                            classname=c['descr'],

                            body=c['subject']+c['catalog_nbr']+c['descr'],

                        )
                        class_data.save()
                      
                        classNumber = str(classNumber)
                        # tutuor_class_data.save()
                        messages.add_message(request, messages.INFO,mark_safe('<a href = /classes/' + classNumber +'>'+subject + catalog_nbr + ": " + name +'</a>'))
            all_classes = Classes.objects.all()
            if len(data) == 0:
                messages.add_message(
                    request, messages.WARNING, 'No classes found')
        else:
            input = input_value.split(' ')
            inputLength = len(input)
            first = input[0].upper()
            if inputLength < 0:
                courseNumber = input[1]
            else:
                url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1232'
                if inputLength == 1:
                    url += '&subject=' + first
                    try:
                        response = requests.get(url)
                        data = response.json()
                    except requests.exceptions.RequestException:
                        url += '&catalog_nbr=' + first
                        response = requests.get(url)
                        data = response.json()
                        if len(data) == 1:
                            currentClasses = []
                            for c in data:
                                name = c['descr']
                                if name in currentClasses:
                                    i = 1
                                else:
                                    currentClasses.append(name)
                                    catalog_nbr = c['catalog_nbr']
                                    subject = c['subject']
                                    classNumber = c['class_nbr']
                                    class_data = Classes(
                                        subject=c['subject'],
                                        catalognumber=c['catalog_nbr'],
                                        classsection=c['class_section'],
                                        classnumber=c['class_nbr'],
                                        classname=c['descr'],

                                        body=c['subject'] + c['catalog_nbr'] + c['descr'],

                                    )
                                    class_data.save()

                                    classNumber = str(classNumber)
                                    # tutuor_class_data.save()
                                    messages.add_message(request, messages.INFO, mark_safe(
                                        '<a href = /classes/' + classNumber + '>' + subject + catalog_nbr + ": " + name + '</a>'))
                elif inputLength == 2:
                    second = request.GET['name'].split(' ')[1]
                    url += '&subject=' + first + '&catalog_nbr=' + second
                    try:
                        response = requests.get(url)
                        data = response.json()
                    except requests.exceptions.RequestException:
                        url += '&keyword=' + request.GET['name']
                        response = requests.get(url)
                        data = response.json()
                elif inputLength == 3:
                    url += '&keyword=' + request.GET['name']
                    response = requests.get(url)
                    data = response.json()
                if len(data) > 1:
                    currentClasses = []
                    for c in data:
                        name = c['descr']
                        if name in currentClasses:
                            i = 1
                        else:
                            currentClasses.append(name)
                            classNumber = c['class_nbr']
                            catalog_nbr = c['catalog_nbr']
                            subject = c['subject']
                            class_data = Classes(
                                subject=c['subject'],
                                catalognumber=c['catalog_nbr'],
                                classsection=c['class_section'],
                                classnumber=c['class_nbr'],
                                classname=c['descr'],

                                body=c['subject'] + c['catalog_nbr'] + c['descr'],

                            )
                            class_data.save()

                            classNumber = str(classNumber)
                            # tutuor_class_data.save()
                            messages.add_message(request, messages.INFO, mark_safe(
                                '<a href = /classes/' + classNumber + '>' + subject + catalog_nbr + ": " + name + '</a>'))
            all_classes = Classes.objects.all()
            if len(data) == 0:
                messages.add_message(
                    request, messages.WARNING, 'No classes found')
    return render(request, 'mainApp/classsearch.html', {'AllClasses': all_classes})

@login_required
def detail(request, classnumber):
    student = request.user
    try:  # check if user is accessing wrong side
        temp = get_object_or_404(Student, user=student)
    except:
        return redirect('tutor')
    model = Classes
    classInfo = Classes.objects.filter(Q(classnumber__icontains=classnumber))
    tutorInfo = tutorClasses.objects.filter(Q(classes__classnumber__icontains=classnumber))
    tutors0 = []
    for i in tutorInfo:
        profile = get_object_or_404(Profile, user=i.tutor)
        tutor = get_object_or_404(Tutor, user=i.tutor)
        tutors0.append((profile, tutor))

    return render(request, 'mainApp/detail.html', {'classinfo': classInfo, 'tutors': tutors0})

@login_required
def tutordetail(request, profileid):
    profile = get_object_or_404(Profile, id=profileid)
    tutorpro = get_object_or_404(Tutor, user=profile.user)
    classesTaught = tutorClasses.objects.filter(tutor=tutorpro.user)
    classes = []
    for i in classesTaught:
        Class = i.classes
        classes.append(Class)
    if request.method == 'POST':
        form = AlertForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.student = request.user
            form.tutor = tutorpro
            form.approved = "pending"
            d = form.date
            classrequested = (form.classname).replace(" ","")
            x = datetime.datetime.strptime(d, '%Y-%m-%d').strftime('%A').lower()
            printx = x.capitalize()
            # messages.add_message(request, messages.INFO, x)
            if x != 'monday' and x != 'tuesday' and x != 'wednesday' and x != 'thursday' and x != 'friday' :
                messages.add_message(request, messages.WARNING, 'Tutor is not available on ' + printx + 's')
                return redirect('tutordetail', profileid=profileid)
            start = x + '_start'
            end = x + '_end'
            # messages.add_message(request, messages.INFO, getattr(tutorpro, start))
            # Check if the session start time is within TA's available hours
            if form.startTime < getattr(tutorpro, start):
                messages.add_message(request, messages.WARNING, 'Start time must be within the available hours')
                return redirect('tutordetail', profileid=profileid)

            # Check if the session end time is within TA's available hours
            elif form.endTime > getattr(tutorpro, end):
                messages.add_message(request, messages.WARNING, 'End time must be within the available hours')
                return redirect('tutordetail', profileid=profileid)
            # Check if the session is no longer than 2 hours
            session_start = datetime.datetime.strptime(form.startTime, '%I:%M %p')
            session_end = datetime.datetime.strptime(form.endTime, '%I:%M %p')
            if (session_end - session_start).total_seconds() > 7200:
                messages.add_message(request, messages.WARNING, 'Session cannot be longer than 2 hours')
                return redirect('tutordetail', profileid=profileid)
            # # Check if the session end time comes after the session start time
            if session_end <= session_start:
                messages.add_message(request, messages.WARNING, 'Session end time must come after the session start time')
                return redirect('tutordetail', profileid=profileid)
            classexistBool = False
            for i in classes:
                if(i.subject+i.catalognumber == classrequested):
                    classexistBool=True
                    break
            if not classexistBool:
                messages.add_message(request, messages.WARNING, "The Tutor doesn't offer this class. Please look at the classes offered below and enter appropriate course mnemoic and catalog number (for ex: CS 3240)")
                return redirect('tutordetail', profileid=profileid)
            else:
                form.save()
                messages.add_message(request, messages.INFO, 'Tutor  request sent!')
                return redirect('tutordetail', profileid=profileid)
    lenclasses = len(classes)
    form = AlertForm()
    
    return render(request, 'mainApp/tutordetail.html', {'info': [(profile, tutorpro, classes,lenclasses)], 'form': form})

@login_required
def classes(request):
    u = request.user
    try:  # check if user is accessing wrong side
        temp = get_object_or_404(Tutor, user=u)
    except:
        return redirect('student')
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

@login_required
def StudentSearch(request):
    student = request.user
    try:  # check if user is accessing wrong side
        temp = get_object_or_404(Student, user=student)
    except:
        return redirect('tutor')
    model = Classes
    data = Classes.objects.all()
    q = request.GET.get('search')
    if q:
        q = q.strip(" ")
        q = q.replace(":","")
        q = q.replace(" ","")
        classes = Classes.objects.filter(
            Q(body__icontains=q) | Q(subject__icontains=q) | Q(classname__icontains=q) | Q(catalognumber__icontains=q)
        )
        return render(request, 'mainApp/classList.html', {'info': classes})
    else:
        return render(request, 'mainApp/classList.html', {'info': data})


@login_required
# the tutor settings that a tutor sees when they first log in (right after initial account settings)
def accountSettings2t(request):
    # u = request.user
    # try:  # check if user is accessing wrong side
    #     temp = get_object_or_404(Tutor, user=u)
    # except:
    #     return redirect('student')
    if request.method == "POST":
        # the tutor form that requires you to add everything
        form = FirstTutorForm(request.POST)
        if form.is_valid():
            hourly_rate = form.cleaned_data['hourly_rate']
            #covers hourly rate being empty
            if not form.data['hourly_rate'] or form.data['hourly_rate'] == None:
                messages.add_message(request, messages.WARNING, 'Hourly rate is required.')
            # check if hourly_rate is less than minimum wage or over 100 dollars
            if hourly_rate < 0 or hourly_rate < 12.5 or hourly_rate > 100:
                if hourly_rate < 0:
                    # If the hourly rate is negative, show an error message
                    messages.add_message(request, messages.ERROR, 'Hourly rate cannot be negative')
                    return redirect('accountSettings2t')
                if hourly_rate < 12.5:
                    messages.add_message(request, messages.ERROR, 'Hourly rate cannot be less than minimum wage')
                    return redirect('accountSettings2t')
                if hourly_rate > 100:
                    messages.add_message(request, messages.ERROR, 'Hourly rate cannot be greater than $100')
            # check that 'Select Time' isn't selected
            if ((form.data['monday_start'] == "Select Time" or form.data['monday_end'] == "Select Time") or \
                    (form.data['tuesday_start'] == "Select Time" or form.data['tuesday_end'] == "Select Time") or \
                    (form.data['wednesday_start'] == "Select Time" or form.data['wednesday_end'] == "Select Time") or \
                    (form.data['thursday_start'] == "Select Time" or form.data['thursday_end'] == "Select Time") or \
                    (form.data['friday_start'] == "Select Time" or form.data['friday_end'] == "Select Time")):
                messages.add_message(request, messages.WARNING, 'You must select an option for every start and end.')
                return redirect('accountSettings2t')
            #start to declare all the time variables needed to compare
            monday_start = form.data['monday_start']
            tuesday_start = form.data['tuesday_start']
            wednesday_start = form.data['wednesday_start']
            thursday_start = form.data['thursday_start']
            friday_start = form.data['friday_start']

            monday_end = form.data['monday_end']
            tuesday_end = form.data['tuesday_end']
            wednesday_end = form.data['wednesday_end']
            thursday_end = form.data['thursday_end']
            friday_end = form.data['friday_end']

            monday_start_hour = monday_start[0]
            tuesday_start_hour = tuesday_start[0]
            wednesday_start_hour = wednesday_start[0]
            thursday_start_hour = thursday_start[0]
            friday_start_hour = friday_start[0]
            if(monday_start != "Not Available" and monday_end != "Not Available"):
            #case for when hour has two digits
                if(monday_start[1] != ":"):
                    monday_start_hour = int(monday_start_hour + monday_start[1])
                    monday_start_minutes = int(monday_start[3:5])
                    monday_start_meridiem = monday_start[6:8]
                else:
                    monday_start_hour = int(monday_start_hour)
                    monday_start_minutes = int(monday_start[2:4])
                    monday_start_meridiem = monday_start[5:7]
                #create monday end variables
                monday_end_hour = monday_end[0]
                if(form.data['monday_end'][1] != ":"):
                    monday_end_hour = int(monday_end_hour + monday_end[1])
                    monday_end_minutes = int(monday_end[3:5])
                    monday_end_meridiem = monday_end[6:8]
                else:
                    monday_end_hour = int(monday_end_hour)
                    monday_end_minutes = int(monday_end[2:4])
                    monday_end_meridiem = monday_end[5:7]
                # check if end time is before start time if meridiems are equal
                if ((monday_end_hour < monday_start_hour and monday_end_meridiem == monday_start_meridiem)):
                    messages.add_message(request, messages.WARNING, 'Monday start time must be after end time')
                    return redirect('accountSettings2t')
                #check if end meridiem is PM and start meridiem is AM
                if(monday_end_meridiem == "AM" and monday_start_meridiem == "PM"):
                    messages.add_message(request, messages.WARNING, 'Monday start time must be after end time')
                    return redirect('accountSettings2t')
                    # if hours and meridiems are equal, check if end minutes is less than start minutes
                if (monday_end_hour == monday_start_hour and monday_end_meridiem == monday_start_meridiem and \
                        monday_end_minutes < monday_start_minutes):
                    messages.add_message(request, messages.WARNING, 'Monday start time must be after end time')
                    return redirect('accountSettings2t')
                #check if times are equal
                if (monday_end_hour == monday_start_hour and monday_end_minutes == monday_start_minutes and \
                        monday_end_meridiem == monday_start_meridiem):
                    messages.add_message(request, messages.WARNING, 'Start time cannot equal end time')
                    return redirect('accountSettings2t')
                #check for case where end time is 12:00 or 12:30 and start time is some time in the afternoon
                if (monday_end_hour == 12 and monday_start_hour < 12 and monday_end_meridiem == "PM" and \
                        monday_start_meridiem == "PM"):
                    messages.add_message(request, messages.WARNING, 'Monday start time must be after end time')
                    return redirect('accountSettings2t')
            if(tuesday_start != "Not Available" and tuesday_end != "Not Available"):
                if (tuesday_start[1] != ":"):
                    tuesday_start_hour = int(tuesday_start_hour + tuesday_start[1])
                    tuesday_start_minutes = int(tuesday_start[3:5])
                    tuesday_start_meridiem = tuesday_start[6:8]
                else:
                    tuesday_start_hour = int(tuesday_start_hour)
                    tuesday_start_minutes = int(tuesday_start[2:4])
                    tuesday_start_meridiem = tuesday_start[5:7]
                tuesday_end_hour = tuesday_end[0]
                if (form.data['tuesday_end'][1] != ":"):
                    tuesday_end_hour = int(tuesday_end_hour + tuesday_end[1])
                    tuesday_end_minutes = int(tuesday_end[3:5])
                    tuesday_end_meridiem = tuesday_end[6:8]
                else:
                    tuesday_end_hour = int(tuesday_end_hour)
                    tuesday_end_minutes = int(tuesday_end[2:4])
                    tuesday_end_meridiem = tuesday_end[5:7]
                # check if end time is before start time if meridiems are equal
                if ((tuesday_end_hour < tuesday_start_hour and tuesday_end_meridiem == tuesday_start_meridiem)):
                    messages.add_message(request, messages.WARNING, 'Tuesday start time must be after end time')
                    return redirect('accountSettings2t')
                # check if end meridiem is PM and start meridiem is AM
                if (tuesday_end_meridiem == "AM" and tuesday_start_meridiem == "PM"):
                    messages.add_message(request, messages.WARNING, 'Tuesday start time must be after end time')
                    return redirect('accountSettings2t')
                    # if hours and meridiems are equal, check if end minutes is less than start minutes
                if (tuesday_end_hour == tuesday_start_hour and tuesday_end_meridiem == tuesday_start_meridiem and \
                        tuesday_end_minutes < tuesday_start_minutes):
                    messages.add_message(request, messages.WARNING, 'Tuesday start time must be after end time')
                    return redirect('accountSettings2t')
                # check if times are equal
                if (tuesday_end_hour == tuesday_start_hour and tuesday_end_minutes == tuesday_start_minutes and \
                        tuesday_end_meridiem == tuesday_start_meridiem):
                    messages.add_message(request, messages.WARNING, 'Start time cannot equal end time')
                    return redirect('accountSettings2t')
                # check for case where end time is 12:00 or 12:30 and start time is some time in the afternoon
                if (tuesday_end_hour == 12 and tuesday_start_hour < 12 and tuesday_end_meridiem == "PM" and \
                        tuesday_start_meridiem == "PM"):
                    messages.add_message(request, messages.WARNING, 'Tuesday start time must be after end time')
                    return redirect('accountSettings2t')
            #wednesday
            if (wednesday_start != "Not Available" and wednesday_end != "Not Available"):
                if (wednesday_start[1] != ":"):
                    wednesday_start_hour = int(wednesday_start_hour + wednesday_start[1])
                    wednesday_start_minutes = int(wednesday_start[3:5])
                    wednesday_start_meridiem = wednesday_start[6:8]
                else:
                    wednesday_start_hour = int(wednesday_start_hour)
                    wednesday_start_minutes = int(wednesday_start[2:4])
                    wednesday_start_meridiem = wednesday_start[5:7]
                wednesday_end_hour = wednesday_end[0]
                if (form.data['wednesday_end'][1] != ":"):
                    wednesday_end_hour = int(wednesday_end_hour + wednesday_end[1])
                    wednesday_end_minutes = int(wednesday_end[3:5])
                    wednesday_end_meridiem = wednesday_end[6:8]
                else:
                    wednesday_end_hour = int(wednesday_end_hour)
                    wednesday_end_minutes = int(wednesday_end[2:4])
                    wednesday_end_meridiem = wednesday_end[5:7]
                # check if end time is before start time if meridiems are equal
                if ((wednesday_end_hour < wednesday_start_hour and wednesday_end_meridiem == wednesday_start_meridiem)):
                    messages.add_message(request, messages.WARNING, 'Wednesday start time must be after end time')
                    return redirect('accountSettings2t')
                # check if end meridiem is PM and start meridiem is AM
                if (wednesday_end_meridiem == "AM" and wednesday_start_meridiem == "PM"):
                    messages.add_message(request, messages.WARNING, 'Wednesday start time must be after end time')
                    return redirect('accountSettings2t')
                    # if hours and meridiems are equal, check if end minutes is less than start minutes
                if (wednesday_end_hour == wednesday_start_hour and wednesday_end_meridiem == wednesday_start_meridiem and \
                        wednesday_end_minutes < wednesday_start_minutes):
                    messages.add_message(request, messages.WARNING, 'Wednesday start time must be after end time')
                    return redirect('accountSettings2t')
                # check if times are equal
                if (wednesday_end_hour == wednesday_start_hour and wednesday_end_minutes == wednesday_start_minutes and \
                        wednesday_end_meridiem == wednesday_start_meridiem):
                    messages.add_message(request, messages.WARNING, 'Start time cannot equal end time')
                    return redirect('accountSettings2t')
                # check for case where end time is 12:00 or 12:30 and start time is some time in the afternoon
                if (wednesday_end_hour == 12 and wednesday_start_hour < 12 and wednesday_end_meridiem == "PM" and \
                        wednesday_start_meridiem == "PM"):
                    messages.add_message(request, messages.WARNING, 'Wednesday start time must be after end time')
                    return redirect('accountSettings2t')
            #thursday
            if (thursday_start != "Not Available" and thursday_end != "Not Available"):
                if (thursday_start[1] != ":"):
                    thursday_start_hour = int(thursday_start_hour + thursday_start[1])
                    thursday_start_minutes = int(thursday_start[3:5])
                    thursday_start_meridiem = thursday_start[6:8]
                else:
                    thursday_start_hour = int(thursday_start_hour)
                    thursday_start_minutes = int(thursday_start[2:4])
                    thursday_start_meridiem = thursday_start[5:7]
                thursday_end_hour = thursday_end[0]
                if (form.data['thursday_end'][1] != ":"):
                    thursday_end_hour = int(thursday_end_hour + thursday_end[1])
                    thursday_end_minutes = int(thursday_end[3:5])
                    thursday_end_meridiem = thursday_end[6:8]
                else:
                    thursday_end_hour = int(thursday_end_hour)
                    thursday_end_minutes = int(thursday_end[2:4])
                    thursday_end_meridiem = thursday_end[5:7]
                # check if end time is before start time if meridiems are equal
                if ((thursday_end_hour < thursday_start_hour and thursday_end_meridiem == thursday_start_meridiem)):
                    messages.add_message(request, messages.WARNING, 'Thursday start time must be after end time')
                    return redirect('accountSettings2t')
                # check if end meridiem is PM and start meridiem is AM
                if (thursday_end_meridiem == "AM" and thursday_start_meridiem == "PM"):
                    messages.add_message(request, messages.WARNING, 'Thursday start time must be after end time')
                    return redirect('accountSettings2t')
                    # if hours and meridiems are equal, check if end minutes is less than start minutes
                if (thursday_end_hour == thursday_start_hour and thursday_end_meridiem == thursday_start_meridiem and \
                        thursday_end_minutes < thursday_start_minutes):
                    messages.add_message(request, messages.WARNING, 'Thursday start time must be after end time')
                    return redirect('accountSettings2t')
                # check if times are equal
                if (thursday_end_hour == thursday_start_hour and thursday_end_minutes == thursday_start_minutes and \
                        thursday_end_meridiem == thursday_start_meridiem):
                    messages.add_message(request, messages.WARNING, 'Start time cannot equal end time')
                    return redirect('accountSettings2t')
                # check for case where end time is 12:00 or 12:30 and start time is some time in the afternoon
                if (thursday_end_hour == 12 and thursday_start_hour < 12 and thursday_end_meridiem == "PM" and \
                        thursday_start_meridiem == "PM"):
                    messages.add_message(request, messages.WARNING, 'Thursday start time must be after end time')
                    return redirect('accountSettings2t')
            #friday
            if (friday_start != "Not Available" and friday_end != "Not Available"):
                if (friday_start[1] != ":"):
                    friday_start_hour = int(friday_start_hour + friday_start[1])
                    friday_start_minutes = int(friday_start[3:5])
                    friday_start_meridiem = friday_start[6:8]
                else:
                    friday_start_hour = int(friday_start_hour)
                    friday_start_minutes = int(friday_start[2:4])
                    friday_start_meridiem = friday_start[5:7]
                friday_end_hour = friday_end[0]
                if (form.data['friday_end'][1] != ":"):
                    friday_end_hour = int(friday_end_hour + friday_end[1])
                    friday_end_minutes = int(friday_end[3:5])
                    friday_end_meridiem = friday_end[6:8]
                else:
                    friday_end_hour = int(friday_end_hour)
                    friday_end_minutes = int(friday_end[2:4])
                    friday_end_meridiem = friday_end[5:7]
                # check if end time is before start time if meridiems are equal
                if ((friday_end_hour < friday_start_hour and friday_end_meridiem == friday_start_meridiem)):
                    messages.add_message(request, messages.WARNING, 'Friday start time must be after end time')
                    return redirect('accountSettings2t')
                # check if end meridiem is PM and start meridiem is AM
                if (friday_end_meridiem == "AM" and friday_start_meridiem == "PM"):
                    messages.add_message(request, messages.WARNING, 'Friday start time must be after end time')
                    return redirect('accountSettings2t')
                    # if hours and meridiems are equal, check if end minutes is less than start minutes
                if (friday_end_hour == friday_start_hour and friday_end_meridiem == friday_start_meridiem and \
                        friday_end_minutes < friday_start_minutes):
                    messages.add_message(request, messages.WARNING, 'Friday start time must be after end time')
                    return redirect('accountSettings2t')
                # check if times are equal
                if (friday_end_hour == friday_start_hour and friday_end_minutes == friday_start_minutes and \
                        friday_end_meridiem == friday_start_meridiem):
                    messages.add_message(request, messages.WARNING, 'Start time cannot equal end time')
                    return redirect('accountSettings2t')
                # check for case where end time is 12:00 or 12:30 and start time is some time in the afternoon
                if (friday_end_hour == 12 and friday_start_hour < 12 and friday_end_meridiem == "PM" and \
                        friday_start_meridiem == "PM"):
                    messages.add_message(request, messages.WARNING, 'Friday start time must be after end time')
                    return redirect('accountSettings2t')
            #check that if 'Not Available' is selected for one of the options, the other must be 'Not Available' as well
            if ((form.data['monday_start'] == "Not Available" and form.data['monday_end'] != "Not Available") or \
                  (form.data['monday_end'] == "Not Available" and form.data['monday_start'] != "Not Available") or \
                  (form.data['tuesday_start'] == "Not Available" and form.data['tuesday_end'] != "Not Available") or \
                  (form.data['tuesday_end'] == "Not Available" and form.data['tuesday_start'] != "Not Available") or \
                  (form.data['wednesday_start'] == "Not Available" and form.data['wednesday_end'] != "Not Available") or \
                  (form.data['wednesday_end'] == "Not Available" and form.data['wednesday_start'] != "Not Available") or \
                  (form.data['thursday_start'] == "Not Available" and form.data['thursday_end'] != "Not Available") or \
                  (form.data['thursday_end'] == "Not Available" and form.data['thursday_start'] != "Not Available") or \
                  (form.data['friday_start'] == "Not Available" and form.data['friday_end'] != "Not Available") or \
                  (form.data['friday_end'] == "Not Available" and form.data['friday_start'] != "Not Available")):
                messages.add_message(request, messages.WARNING, '"Not Available" must be selected for both start and end')
            #check that if both inputs are not "Not Available," then they should not be equal to each other
            #check that end time is after start time
            else:
                tutor = form.save(commit=False)
                tutor.user = request.user  # connects the tutor to the user
                tutor.save()
                return redirect('classes')  # send them to the classes page
        else:
            messages.add_message(request, messages.WARNING, 'One or more fields are invalid.')
            return redirect('accountSettings2t')
    form = FirstTutorForm()
    return render(request, 'mainApp/accountSettings2t.html', {"form": form})

@login_required
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

@login_required
def accountDisplay(request):
    user = request.user #using this to access the profile of the user logged in
    profile = get_object_or_404(Profile, user=user) #profile of the user logged in
    tutor = get_object_or_404(Tutor, user=user) #tutor of the user logged in
    classes_offered = tutorClasses.objects.filter(tutor=tutor.user)
    return render(request, 'mainApp/accountDisplay.html', {"profile": profile, "tutor": tutor,"classes_offered": classes_offered})

@login_required
def accountDisplayStudent(request): #the user version of account display
    user = request.user #using this to access the profile of the user logged in
    profile = get_object_or_404(Profile, user=user) #profile of the user logged in
    return render(request, 'mainApp/accountDisplayStudent.html', {"profile": profile})


def checkTimes(first, second):
    session_start = datetime.datetime.strptime(first, '%I:%M %p')
    session_end = datetime.datetime.strptime(second, '%I:%M %p')
    if session_start == session_end:
        return False
    if session_end > session_start:
        return False
    else:
        return True


class CalendarView(generic.ListView):
    model = Request
    template_name = 'mainApp/tutorCalendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        # d = get_date(self.request.GET.get('day', None))
        d = get_date(self.request.GET.get('month', None))

        # get user
        user = self.request.user

        # Instantiate our calendar class with today's year and date and user
        cal = Calendar(d.year, d.month, user)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['tutorCalendar'] = mark_safe(html_cal)

        # d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - datetime.timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + datetime.timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.datetime.today()
