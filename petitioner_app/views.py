from mailmerge import MailMerge
from django.shortcuts import render
from .forms import VehRegisterForm
from django.template import loader
from django.http import HttpResponse
from petitioner_app.models import Application
import subprocess


# Create your views here.


def landing(request):
    template = loader.get_template('petitioner_app/landing_page.html')
    return HttpResponse(template.render({}, request))


def vehregister(request):
    form = VehRegisterForm(request.POST or None)

    if request.method == 'POST':
        form = VehRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            form_dict = form.data.dict()
            template = "petitioner_app\\templates\\converter\\formTemplate.docx"
            output_document = "output.docx"
            libre_office_path = 'C:\\Program Files\\LibreOffice\\program\\soffice'
            # Create docx file due to template
            document = MailMerge(template)
            document.merge_pages([form_dict])
            document.write(output_document)
            document.close()
            # Convert docx to pdf (using libreoffice)
            args = [libre_office_path, '--headless', '--convert-to', 'pdf', output_document]
            subprocess.run(args)
            # Create an application
            application = Application(petitioner=request.user, form=form.instance)
            application.save()

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
