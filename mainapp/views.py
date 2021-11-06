from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import RegisterForm


def index(request):
    template = loader.get_template('mainapp/index.html')
    return HttpResponse(template.render({}, request))


def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/main")
    else:
        form = RegisterForm()
    return render(response, "registration/register.html", {"form": form})
