from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import RegisterForm
from .forms import ProfileForm


def index(request):
    template = loader.get_template('mainapp/index.html')
    return HttpResponse(template.render({}, request))


def register(response):
    if response.method == "POST":
        user_form = RegisterForm(response.POST)
        profile_form = ProfileForm(response.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.instance.user = user_form.instance
            profile_form.save()
            return redirect("/main")
    else:
        user_form = RegisterForm()
        profile_form = ProfileForm()
    return render(response, "registration/register.html", {
        'user_form': user_form,
        'profile_form': profile_form
    })

