from mailmerge import MailMerge
from django.shortcuts import render, redirect
from .forms import VehRegisterForm, VehDeregisterForm
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
            # Docs
            template = "petitioner_app\\templates\\converter\\formTemplate.docx"
            output_document = "petitioner_app\\templates\\converter\\output.docx"
            output_pdf = "petitioner_app\\templates\\converter\\output.pdf"
            document = MailMerge(template)
            document.merge_pages([form_dict])
            document.write(output_document)
            document.close()
            form.save()
            
            # PDF
            xml = "petitioner_app\\templates\\converter\\input.xml"
            # Path to destination PDF file
            pdf = "petitioner_app\\templates\\converter\\output.pdf"
            doc = XMLtoPDF(xml, pdf)
            # Convert to PDF format
            doc.createPDF_register()
            # Save PDF
            doc.savePDF()

    context = {'form': form}
    return render(request, "petitioner_app/vehregister.html", context)


def vehderegister(request):
    form = VehDeregisterForm(request.POST or None)

    if request.method == 'POST':
        xml = "petitioner_app\\templates\\converter\\input_dereg.xml"
        # Path to destination PDF file
        pdf = "petitioner_app\\templates\\converter\\output_dereg.pdf"
        doc = XMLtoPDF(xml, pdf)
        # Convert to PDF format
        doc.createPDF_deregister()
        # Save PDF
        doc.savePDF()
        form = VehDeregisterForm(request.POST or None)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, "petitioner_app/vehderegister.html", context)


def form3(request):
    template = loader.get_template('petitioner_app/form3.html')
    return HttpResponse(template.render({}, request))


def myforms(request):
    template = loader.get_template('petitioner_app/myforms.html')
    return HttpResponse(template.render({}, request))
