from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    Clerk = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ["Clerk", "username", "first_name", "last_name", "email", "password1", "password2"]

