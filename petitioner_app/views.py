from django.shortcuts import render, redirect
from .forms import VehRegisterForm
from django.template import loader
from django.http import HttpResponse

# Create your views here.
from .templates.converter.xmlToPdf import XMLtoPDF


def landing(request):
    template = loader.get_template('petitioner_app/landing_page.html')
    return HttpResponse(template.render({}, request))


def vehregister(request):
    form = VehRegisterForm(request.POST or None)

    if request.method == 'POST':
        xml = "petitioner_app/templates/converter/input.xml"
        # Path to destination PDF file
        pdf = "petitioner_app/templates/converter/output.pdf"
        doc = XMLtoPDF(xml, pdf)
        # Convert to PDF format
        doc.createPDF()
        # Save PDF
        doc.savePDF()
        form = VehRegisterForm(request.POST or None)
        if form.is_valid():
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
