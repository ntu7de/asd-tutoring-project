from django import forms
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
        exclude = ()
