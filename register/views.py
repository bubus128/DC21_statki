from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import VehRegisterForm
# Create your views here.


def vehregister(request):
    form = VehRegisterForm(request.POST or None)

    if request.method == 'POST':
        form = VehRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, "formularze/vehregister.html", context)


def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/main")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})
