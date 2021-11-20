from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.
class VehRegister(models.Model):
    id = models.BigAutoField(primary_key=True)

    class rodzajPojazdu(models.TextChoices):
        NOWY = 'Nowy',
        UZYWANY = 'Uzywany',
        ZABYTKOWY = 'Zabytkowy',
        SAMODZIELNY = 'Samodzielnie zrobiony',

    EURO = "Pojazd ma dopuszczenie indywidualne europejskie WE"
    JEDNOSTKOWE = "Pojazd ma dopuszczenie jednostkowe"
    dopuszczenie = [
        (EURO, _('Pojazd ma dopuszczenie indywidualne europejskie WE')),
        (JEDNOSTKOWE, _('Pojazd ma dopuszczenie jednostkowe')),
    ]

    rodzaj_pojazdu = models.CharField(
        max_length=21,
        choices=rodzajPojazdu.choices,
        default=rodzajPojazdu.NOWY,
    )
    rok_produkcji = models.DecimalField(decimal_places=0, max_digits=4, default=2021, blank=True, null=True)
    waga = models.DecimalField(decimal_places=2, max_digits=10000, default=0, blank=True, null=True)
    dlugosc = models.DecimalField(decimal_places=2, max_digits=10000, default=0, blank=True, null=True)
    szerokosc = models.DecimalField(decimal_places=2, max_digits=10000, default=0, blank=True, null=True)
    glebokosc_zanurzenia = models.DecimalField(decimal_places=2, max_digits=10000, default=0, blank=True, null=True)
    wysokosc_nad_poziomem_wody = models.DecimalField(decimal_places=2, max_digits=10000, default=0, blank=True,
                                                     null=True)
    dopuszczenie_pojazdu = models.CharField(max_length=100, choices=dopuszczenie, default=EURO, blank=True, null=True)
    dowod_potwierdzajacy_wlasnosc = models.FileField(blank=True, null=True)


class VehDeregister(models.Model):
    vehicle_id = models.CharField(max_length=10, blank=True, null=True)
    reason = models.CharField(max_length=250, blank=True, null=True)
    proof_of_ownership = models.FileField(blank=True, null=True)


class VehReregister(models.Model):
    current_owner_id = models.CharField(max_length=10, blank=True, null=True)
    new_owner_id = models.CharField(max_length=10, blank=True, null=True)
    proof_of_ownership = models.FileField(blank=True, null=True)


class Application(models.Model):
    id = models.BigAutoField(primary_key=True)
    form = models.ForeignKey(VehRegister, on_delete=models.CASCADE)
    petitioner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="refers_to")
    clerk = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_case")


class Document(models.Model):
    id = models.BigAutoField(primary_key=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    filename = models.CharField(max_length=60)
    path = models.CharField(max_length=200)
