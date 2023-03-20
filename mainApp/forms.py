from django import forms
from django.contrib.auth.models import User
from .models import Profile, Tutor, Student


class ProfileForm(forms.ModelForm): #the form you see when you first log in to input your profile information
    #all of the fields you input
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    year = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    pronouns = forms.CharField(required=True, max_length=20)
    major = forms.CharField(required=True, max_length=100)
    is_tutor = forms.BooleanField(required=False)
    is_student = forms.BooleanField(required=False)
    fun_fact = forms.CharField(required=True, max_length=200)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'year', 'email', 'pronouns', 'major', 'is_tutor', 'is_student', 'fun_fact']
        exclude = ()


class ProfileForm2(forms.ModelForm): #the form you see that updates your profile in "Account Settings"
    #the fields you can (BUT DON'T HAVE TO) update
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    year = forms.IntegerField(required=False)
    email = forms.EmailField(required=False)
    pronouns = forms.CharField(max_length=20, required=False)
    major = forms.CharField(max_length=100, required=False)
    fun_fact = forms.CharField(max_length=200, required=False)
    edit_profile = forms.BooleanField(widget=forms.HiddenInput, initial=True) #allows me to differentiate between the profile and the tutor/student forms
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'year', 'email', 'pronouns', 'major', 'fun_fact']
        exclude = ()


class TutorForm(forms.ModelForm):#the form you see that updates your tutor settings in "Account Settings"
    #the fields you can (BUT DON'T HAVE TO) update
    hourly_rate = forms.FloatField(required=False)
    monday_hours = forms.CharField(required=False)
    tuesday_hours = forms.CharField(required=False)
    wednesday_hours = forms.CharField(required=False)
    thursday_hours = forms.CharField(required=False)
    friday_hours = forms.CharField(required=False)
    edit_tutor = forms.BooleanField(widget=forms.HiddenInput, initial=True) #differentiates between profile and tutor forms

    class Meta:
        model = Tutor
        fields = ['hourly_rate', 'monday_hours', 'tuesday_hours', 'wednesday_hours', 'thursday_hours', 'friday_hours']
        exclude = ()


class FirstTutorForm(forms.ModelForm): #the form that you go to after first making your profile as a tutor
    #the fields you MUST fill out
    hourly_rate = forms.FloatField(required=False)
    monday_hours = forms.CharField(required=False)
    tuesday_hours = forms.CharField(required=False)
    wednesday_hours = forms.CharField(required=False)
    thursday_hours = forms.CharField(required=False)
    friday_hours = forms.CharField(required=False)

    class Meta:
        model = Tutor
        fields = ['hourly_rate', 'monday_hours', 'tuesday_hours', 'wednesday_hours', 'thursday_hours', 'friday_hours']
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
