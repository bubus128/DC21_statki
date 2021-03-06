from mailmerge import MailMerge
from django.shortcuts import render
from .forms import VehRegisterForm, VehDeregisterForm, VehReregisterForm
from .models import VehRegister, VehDeregister, VehReregister, Application
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
import random
import subprocess
import petitioner_app.templates.uploader.uploader as uploader
from os.path import splitext
from sys import platform


def landing(request):
    template = loader.get_template('petitioner_app/landing_page.html')
    return HttpResponse(template.render({}, request))


def vehregister(request):
    form = VehRegisterForm(request.POST or None)

    if request.method == 'POST':
        form = VehRegisterForm(request.POST or None)
        print(form)
        if form.is_valid():
            form_dict = form.data.dict()
            print(form_dict)
            template = "petitioner_app\\templates\\converter\\formTemplate.docx"
            if platform == "linux":
                template = "petitioner_app/templates/converter/formTemplate.docx"
            output_document = "output1.docx"
            libre_office_path = 'C:\\Program Files\\LibreOffice\\program\\soffice'
            if platform == "linux":
                libre_office_path = 'libreoffice'

            # Create docx file due to template
            document = MailMerge(template)
            document.merge_pages([form_dict])
            document.write(output_document)
            document.close()
            u = uploader.Uploader()
            doc_id = u.upload(output_document)

            # Convert docx to pdf (using libreoffice)
            args = [libre_office_path, '--headless', '--convert-to', 'pdf', output_document]
            subprocess.run(args)
            pdf_id = u.upload(splitext(output_document)[0]+".pdf")

            # Create an application
            clerks = User.objects.filter(profile__role="clerk")
            clerk = clerks[random.randint(0, len(clerks)-1)]
            application = Application(petitioner=request.user, vehregister_form=form.instance, clerk=clerk)
            form_object = form.save()

            # store the links
            form_object.doc_link = u.get_link(doc_id)
            form_object.pdf_link = u.get_link(pdf_id)
            form_object.save()
            application.save()

    context = {'form': form}
    return render(request, "petitioner_app/vehregister.html", context)


def vehderegister(request):
    form = VehDeregisterForm(request.POST or None)

    if request.method == 'POST':
        form = VehDeregisterForm(request.POST or None)
        if form.is_valid():
            form_dict = form.data.dict()
            form_dict['rodzaj_pojazdu'] = form_dict.pop('vehicle_id')
            form_dict['rok_produkcji'] = form_dict.pop('reason')
            template = "petitioner_app\\templates\\converter\\form2Template.docx"
            if platform == "linux":
                template = "petitioner_app/templates/converter/form2Template.docx"
            output_document = "output2.docx"
            libre_office_path = 'C:\\Program Files\\LibreOffice\\program\\soffice'
            if platform == "linux":
                libre_office_path = 'libreoffice'

            # Create docx file due to template
            document = MailMerge(template)
            document.merge_pages([form_dict])
            document.write(output_document)
            document.close()
            u = uploader.Uploader()
            doc_id = u.upload(output_document)

            # Convert docx to pdf (using libreoffice)
            args = [libre_office_path, '--headless', '--convert-to', 'pdf', output_document]
            subprocess.run(args)
            pdf_id = u.upload(splitext(output_document)[0]+".pdf")

            # Create an application
            clerks = User.objects.filter(profile__role="clerk")
            clerk = clerks[random.randint(0, len(clerks)-1)]
            application = Application(petitioner=request.user, vehderegister_form=form.instance, clerk=clerk)
            form_object = form.save()

            # store the links
            form_object.doc_link = u.get_link(doc_id)
            form_object.pdf_link = u.get_link(pdf_id)
            form_object.save()
            application.save()

    context = {'form': form}
    return render(request, "petitioner_app/vehderegister.html", context)


def vehreregister(request):
    form = VehReregisterForm(request.POST or None)

    if request.method == 'POST':
        form = VehReregisterForm(request.POST or None)
        if form.is_valid():
            form_dict = form.data.dict()
            form_dict['rodzaj_pojazdu'] = form_dict.pop('current_owner_id')
            form_dict['rok_produkcji'] = form_dict.pop('new_owner_id')
            template = "petitioner_app\\templates\\converter\\form3Template.docx"
            if platform == "linux":
                template = "petitioner_app/templates/converter/form3Template.docx"
            output_document = "output3.docx"
            libre_office_path = 'C:\\Program Files\\LibreOffice\\program\\soffice'
            if platform == "linux":
                libre_office_path = 'libreoffice'

            # Create docx file due to template
            document = MailMerge(template)
            document.merge_pages([form_dict])
            document.write(output_document)
            document.close()
            u = uploader.Uploader()
            doc_id = u.upload(output_document)

            # Convert docx to pdf (using libreoffice)
            args = [libre_office_path, '--headless', '--convert-to', 'pdf', output_document]
            subprocess.run(args)
            pdf_id = u.upload(splitext(output_document)[0]+".pdf")

            # Create an application
            clerks = User.objects.filter(profile__role="clerk")
            clerk = clerks[random.randint(0, len(clerks)-1)]
            application = Application(petitioner=request.user, vehreregister_form=form.instance, clerk=clerk)
            form_object = form.save()

            # store the links
            form_object.doc_link = u.get_link(doc_id)
            form_object.pdf_link = u.get_link(pdf_id)
            form_object.save()
            application.save()

    context = {'form': form}
    return render(request, "petitioner_app/vehreregister.html", context)


def myforms(request):
    current_user_id = request.user.id
    my_applications = Application.objects.filter(petitioner=current_user_id)
    template = loader.get_template('petitioner_app/myforms.html')
    vehregister_forms = []
    vehderegister_forms = []
    vehreregister_forms = []

    for application in my_applications:

        if application.vehregister_form is not None:
            vehregister_forms.append(application.vehregister_form)
        elif application.vehderegister_form is not None:
            vehderegister_forms.append(application.vehderegister_form)
        elif application.vehreregister_form is not None:
            vehreregister_forms.append(application.vehreregister_form)

    context = {
        'vehregister_forms': vehregister_forms,
        'vehderegister_forms': vehderegister_forms,
        'vehreregister_forms': vehreregister_forms,
    }

    return HttpResponse(template.render(context, request))


def singleform(request, form_type, form_id):

    template = loader.get_template('petitioner_app/singleform.html')

    if form_type == "vehregister":
        form = VehRegister.objects.filter(id=form_id)

        context = {
            'form_type': "vehregister",
            'form': form[0],
        }
        return HttpResponse(template.render(context, request))
    elif form_type == "vehderegister":
        form = VehDeregister.objects.filter(id=form_id)

        context = {
            'form_type': "vehderegister",
            'form': form[0],
        }
        return HttpResponse(template.render(context, request))
    elif form_type == "vehreregister":
        form = VehReregister.objects.filter(id=form_id)

        context = {
            'form_type': "vehreregister",
            'form': form[0],
        }
        return HttpResponse(template.render(context, request))
