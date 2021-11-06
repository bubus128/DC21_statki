from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def landing(request):
    template = loader.get_template('clerk_app/landing_page.html')
    return HttpResponse(template.render({}, request))


def myissues(request):
    template = loader.get_template('clerk_app/my_issues.html')
    return HttpResponse(template.render({}, request))
