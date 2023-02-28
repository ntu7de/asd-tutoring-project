from django import forms
from django.contrib.auth.models import User
from .models import Profile


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
