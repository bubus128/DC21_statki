from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class VehRegister(models.Model):
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
    wysokosc_nad_poziomem_wody = models.DecimalField(decimal_places=2, max_digits=10000, default=0, blank=True, null=True)
    dopuszczenie_pojazdu = models.CharField(max_length=100, choices=dopuszczenie,  default=EURO, blank=True, null=True)
    dowod_potwierdzajacy_wlasnosc = models.FileField(blank=True, null=True)
