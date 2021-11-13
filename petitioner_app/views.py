from mailmerge import MailMerge
from django.shortcuts import render, redirect
from .forms import VehRegisterForm
from django.template import loader
from django.http import HttpResponse
import win32com.client

# Create your views here.


def landing(request):
    template = loader.get_template('petitioner_app/landing_page.html')
    return HttpResponse(template.render({}, request))


def vehregister(request):
    form = VehRegisterForm(request.POST or None)

    if request.method == 'POST':
        form = VehRegisterForm(request.POST or None)
        form_dict = form.data.dict()
        if form.is_valid():
            template = "petitioner_app\\templates\\converter\\formTemplate.docx"
            output_document = "petitioner_app\\templates\\converter\\output.docx"
            output_pdf = "petitioner_app\\templates\\converter\\output.pdf"
            document = MailMerge(template)
            document.merge_pages([form_dict])
            document.write(output_document)
            document.close()
            form.save()

    context = {'form': form}
    return render(request, "petitioner_app/vehregister.html", context)


def form2(request):
    template = loader.get_template('petitioner_app/form2.html')
    return HttpResponse(template.render({}, request))


def form3(request):
    template = loader.get_template('petitioner_app/form3.html')
    return HttpResponse(template.render({}, request))


def myforms(request):
    template = loader.get_template('petitioner_app/myforms.html')
    return HttpResponse(template.render({}, request))
