from django import forms
from django.contrib.auth.models import User

from .models import  Profile
from .models import Tutor
from .models import Student, Request
import datetime
from django.core.exceptions import ValidationError
Search = ( ("option1", "course mnemonic"),
           ("option2","course number"),
           ("option1", "course name")
           ) #choices for the search choice field

Years1 =(
    ("First", "First"),
    ("Second", "Second"),
    ("Third", "Third"),
    ("Fourth", "Fourth"), ("Grad", "Grad")
) #choices for the year choice field
Years =(
    ("Select a Year", "Select a Year"),
    ("First", "First"),
    ("Second", "Second"),
    ("Third", "Third"),
    ("Fourth", "Fourth"), ("Grad", "Grad")
) #choices for the year choice field

TimeSelections1 = (
    ("Select Time", "Select Time"),
    ("9:00 AM", "9:00 AM"),
    ("9:30 AM", "9:30 AM"),
    ("10:00 AM", "10:00 AM"),
    ("10:30 AM", "10:30 AM"),
    ("11:00 AM", "11:00 AM"),
    ("11:30 AM", "11:30 AM"),
    ("12:00 PM", "12:00 PM"),
    ("12:30 PM", "12:30 PM"),
    ("1:00 PM", "1:00 PM"),
    ("1:30 PM", "1:30 PM"),
    ("2:00 PM", "2:00 PM"),
    ("2:30 PM", "2:30 PM"),
    ("3:00 PM", "3:00 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4:00 PM", "4:00 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5:00 PM", "5:00 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6:00 PM", "6:00 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7:00 PM", "7:00 PM"),
    ("7:30 PM", "7:30 PM"),
    ("8:00 PM", "8:00 PM"),
) #choices for the time choice field

TimeSelections = (

    ("Select Time", "Select Time"),
    ("Not Available", "Not Available"),
    ("9:00 AM", "9:00 AM"),
    ("9:30 AM", "9:30 AM"),
    ("10:00 AM", "10:00 AM"),
    ("10:30 AM", "10:30 AM"),
    ("11:00 AM", "11:00 AM"),
    ("11:30 AM", "11:30 AM"),
    ("12:00 PM", "12:00 PM"),
    ("12:30 PM", "12:30 PM"),
    ("1:00 PM", "1:00 PM"),
    ("1:30 PM", "1:30 PM"),
    ("2:00 PM", "2:00 PM"),
    ("2:30 PM", "2:30 PM"),
    ("3:00 PM", "3:00 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4:00 PM", "4:00 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5:00 PM", "5:00 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6:00 PM", "6:00 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7:00 PM", "7:00 PM"),
    ("7:30 PM", "7:30 PM"),
    ("8:00 PM", "8:00 PM"),
) #choices for the time choice field

Years1 =(
    ("First", "First"),
    ("Second", "Second"),
    ("Third", "Third"),
    ("Fourth", "Fourth"), ("Grad", "Grad")
)

Pronouns1 = (
    ("She/Her", "She/Her"),
    ("He/Him", "He/Him"),
    ("They/Them", "They/Them"),
    ("She/They", "She/They"), ("He/They", "He/They"), ("Other", "Other")
) #choices for the year choice field

Pronouns = (
    ("Select Pronouns", "Select Pronouns"),
    ("She/Her", "She/Her"),
    ("He/Him", "He/Him"),
    ("They/Them", "They/Them"),
    ("She/They", "She/They"), ("He/They", "He/They"), ("Other", "Other")
) #choices for the year choice field
Days = (
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday")
) #choices for the day choice field

class SearchForm(forms.Form): #the form you see when searching for classes
    search = forms.ChoiceField(choices=Search, required=True)

class ProfileForm(forms.ModelForm): #the form you see when you first log in to input your profile information
    #all of the fields you input
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ex: Jim'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ex: Ryan'}), required=True)
    year = forms.ChoiceField(choices=Years1, required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'ex: jimryan@virginia.edu'}), required=True)
    pronouns = forms.ChoiceField(choices=Pronouns1, required=True)
    major = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ex: Computer Science'}), required=True, max_length=100)
    tutor_or_student = forms.ChoiceField(choices=(("Tutor", 'Tutor'), ("Student", 'Student')), widget=forms.RadioSelect,
                                         required=True)
    fun_fact = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ex: This is my fun fact!'}), required=True, max_length=200)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'year', 'email', 'pronouns', 'major', 'fun_fact', 'tutor_or_student']
        exclude = ()


class ProfileForm2(forms.ModelForm): #the form you see that updates your profile in "Account Settings"
    #the fields you can (BUT DON'T HAVE TO) update
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ex: Jim'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ex: Ryan'}), required=False)
    year = forms.ChoiceField(choices=Years, required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'ex: jimryan@virginia.edu'}), required=False)
    pronouns = forms.ChoiceField(choices=Pronouns, required=False)
    major = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ex: Computer Science'}), max_length=100, required=False)
    fun_fact = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ex: This is my fun fact!'}), max_length=200, required=False)
    edit_profile = forms.BooleanField(widget=forms.HiddenInput, initial=True) #allows me to differentiate between the profile and the tutor/student forms
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'year', 'email', 'pronouns', 'major', 'fun_fact']
        exclude = ()


class TutorForm(forms.ModelForm):#the form you see that updates your tutor settings in "Account Settings"
    #the fields you can (BUT DON'T HAVE TO) update
    hourly_rate = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder':'ex: 12.50'}), required=False)
    monday_start = forms.ChoiceField(choices=TimeSelections, required=False)
    monday_end = forms.ChoiceField(choices=TimeSelections, required=False)
    tuesday_start = forms.ChoiceField(choices=TimeSelections, required=False)
    tuesday_end = forms.ChoiceField(choices=TimeSelections, required=False)
    wednesday_start = forms.ChoiceField(choices=TimeSelections, required=False)
    wednesday_end = forms.ChoiceField(choices=TimeSelections, required=False)
    thursday_start = forms.ChoiceField(choices=TimeSelections, required=False)
    thursday_end = forms.ChoiceField(choices=TimeSelections, required=False)
    friday_start = forms.ChoiceField(choices=TimeSelections, required=False)
    friday_end = forms.ChoiceField(choices=TimeSelections, required=False)
    # monday_hours = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ex: 9:00 AM - 12:00 PM'}), required=False)
    # tuesday_hours = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ex: 9:00 AM - 12:00 PM'}), required=False)
    # wednesday_hours = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ex: 9:00 AM - 12:00 PM'}), required=False)
    # thursday_hours = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ex: 9:00 AM - 12:00 PM'}), required=False)
    # friday_hours = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ex: 9:00 AM - 12:00 PM'}), required=False)
    edit_tutor = forms.BooleanField(widget=forms.HiddenInput, initial=True) #differentiates between profile and tutor forms

    class Meta:
        model = Tutor
        fields = ['hourly_rate', 'monday_start', 'monday_end', 'tuesday_start', 'tuesday_end', 'wednesday_start', 'wednesday_end', 'thursday_start', 'thursday_end', 'friday_start', 'friday_end']
        # fields = ['hourly_rate', 'monday_hours', 'tuesday_hours', 'wednesday_hours', 'thursday_hours', 'friday_hours']
        exclude = ()


class FirstTutorForm(forms.ModelForm): #the form that you go to after first making your profile as a tutor
    #the fields you MUST fill out
    hourly_rate = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder':'ex: 12.50'}), required=False)

    monday_start = forms.ChoiceField(choices=TimeSelections, required=False, initial='Not Available')
    monday_end = forms.ChoiceField(choices=TimeSelections, required=False, initial='Not Available')
    tuesday_start = forms.ChoiceField(choices=TimeSelections, required=False, initial='Not Available')
    tuesday_end = forms.ChoiceField(choices=TimeSelections, required=False, initial='Not Available')
    wednesday_start = forms.ChoiceField(choices=TimeSelections, required=False, initial='Not Available')
    wednesday_end = forms.ChoiceField(choices=TimeSelections, required=False, initial='Not Available')
    thursday_start = forms.ChoiceField(choices=TimeSelections, required=False, initial='Not Available')
    thursday_end = forms.ChoiceField(choices=TimeSelections, required=False, initial='Not Available')
    friday_start = forms.ChoiceField(choices=TimeSelections, required=False, initial='Not Available')
    friday_end = forms.ChoiceField(choices=TimeSelections, required=False, initial='Not Available')


    class Meta:
        model = Tutor
        fields = ['hourly_rate', 'monday_start', 'monday_end', 'tuesday_start', 'tuesday_end', 'wednesday_start', 'wednesday_end', 'thursday_start', 'thursday_end', 'friday_start', 'friday_end']
        # fields = ['hourly_rate', 'monday_hours', 'tuesday_hours', 'wednesday_hours', 'thursday_hours', 'friday_hours']
        exclude = ()

class AlertForm(forms.ModelForm):
    startTime = forms.ChoiceField(choices=TimeSelections1, label="start time")
    endTime = forms.ChoiceField(choices=TimeSelections1, label="end time")
    date = forms.DateField(widget=forms.SelectDateWidget, label="date", initial=datetime.date.today)
    location = forms.CharField(max_length=100, label="location")
    classname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ex: CS 3100 or CS 1110'}), label="class name")
    # tutor = forms.CharField(max_length=100)

    class Meta:
        model = Request
        fields = ['startTime', 'endTime', 'date', 'location','classname']
        exclude = ()


class StudentForm(forms.ModelForm): #the form you see that updates your student settings in "Account Settings"
    #the fields you can (BUT DON'T HAVE TO) update
    classes = forms.CharField(required=False)
    edit_student = forms.BooleanField(widget=forms.HiddenInput, initial=True) #differentiates between profile and student forms

    class Meta:
        model = Student
        fields = ['classes']
        exclude = ()


class FirstStudentForm(forms.ModelForm):#the form that you go to after first making your profile as a student
    #the fields you MUST fill out
    classes = forms.CharField(required=True)

    class Meta:
        model = Student
        fields = ['classes']
        exclude = ()
