from .models import VehRegister, VehDeregister, VehReregister
from django.forms import ModelForm


class VehRegisterForm(ModelForm):

    class Meta:
        model = VehRegister
        exclude = ["doc_link","pdf_link"]


class VehDeregisterForm(ModelForm):

    class Meta:
        model = VehDeregister
        exclude = ["doc_link","pdf_link"]


class VehReregisterForm(ModelForm):

    class Meta:
        model = VehReregister
        exclude = ["doc_link","pdf_link"]