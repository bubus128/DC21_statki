from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import VehRegister
from django.forms import ModelForm


class VehRegisterForm(ModelForm):

    class Meta:
        model = VehRegister
        fields = '__all__'


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

