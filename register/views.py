from django.shortcuts import render, redirect
from .forms import VehRegisterForm

# Create your views here.
from .templates.converter.xmlToPdf import XMLtoPDF


def vehregister(request):
    form = VehRegisterForm(request.POST or None)

    if request.method == 'POST':
        xml = "C:\\Users\\nukee\\OneDrive\\Dokumenty\\GitHub\\merge\\register\\templates\\converter\\input.xml"
        xml = "register\\templates\\converter\\input.xml"
        # Path to destination PDF file
        pdf = "register\\templates\\converter\\output.pdf"
        doc = XMLtoPDF(xml, pdf)
        # Convert to PDF format
        doc.createPDF()
        # Save PDF
        doc.savePDF()
        form = VehRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, "formularze/vehregister.html", context)

