from django import forms
from django.contrib.auth.models import User
from .models import Profile, Tutor, Student


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    year = forms.IntegerField()
    email = forms.EmailField()
    pronouns = forms.CharField(max_length=20)
    major = forms.CharField(max_length=100)
    is_tutor = forms.BooleanField(required=False)
    is_student = forms.BooleanField(required=False)
    fun_fact = forms.CharField(max_length=200)
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'year', 'email', 'pronouns', 'major', 'is_tutor', 'is_student', 'fun_fact']
        exclude = ()

class ProfileForm2(forms.ModelForm):
    edit_profile = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'year', 'email', 'pronouns', 'major', 'fun_fact']
        exclude = ()

class TutorForm(forms.ModelForm):
    # classes = forms.CharField(required=True)
    # hourly_rate = forms.FloatField(required=True)
    edit_tutor = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Tutor
        fields = [ 'monday_hours', 'tuesday_hours', 'wednesday_hours', 'thursday_hours', 'friday_hours', 'hourly_rate']
        exclude = ()

class StudentForm(forms.ModelForm):
    # classes = forms.CharField(required=True)
    # hourly_rate = forms.FloatField(required=True)
    edit_student = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Student
        fields = ['classes']
        exclude = ()
