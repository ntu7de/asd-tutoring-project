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

def tutor(request):
    return render(request, 'mainApp/tutor.html')

def student(request):
    return render(request, 'mainApp/student.html')
@login_required
def accountSettings(request):
    return render(request, 'mainApp/accountSettings.html')

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
