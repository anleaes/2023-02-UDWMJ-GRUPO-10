from django import forms
from django.contrib.auth.models import User

# Create your models here.

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

class UserChangeInformationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']