from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from . import models

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class SubmitProject(ModelForm):
    class Meta:
        model = models.Project
        fields = '__all__'
        exclude = ['user','likes']