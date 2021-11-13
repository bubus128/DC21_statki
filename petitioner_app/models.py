from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class VehRegister(models.Model):
    class rodzajPojazdu(models.TextChoices):
        NEW = 'Nowy',
        USED = 'Uzywany',
        ANTIQUE = 'Zabytkowy',

    EURO = "The vehicle has EC individual homologation"
    JEDNOSTKOWE = "The vehicle has a unit approval"
    dopuszczenie = [
        (EURO, _('The vehicle has EC individual homologation')),
        (JEDNOSTKOWE, _('The vehicle has a unit approval')),
        ]

    type_of_vehicle = models.CharField(
        max_length=21,
        choices=rodzajPojazdu.choices,
        default=rodzajPojazdu.NEW,
    )
    year_of_production = models.DecimalField(decimal_places=0, max_digits=4, default=2021, blank=True, null=True)
    weight = models.DecimalField(decimal_places=2, max_digits=10000, default=0, blank=True, null=True)
    lenght = models.DecimalField(decimal_places=2, max_digits=10000, default=0, blank=True, null=True)
    width = models.DecimalField(decimal_places=2, max_digits=10000, default=0, blank=True, null=True)
    immersion_depth = models.DecimalField(decimal_places=2, max_digits=10000, default=0, blank=True, null=True)
    high_water_mark = models.DecimalField(decimal_places=2, max_digits=10000, default=0, blank=True, null=True)
    vehicle_approval = models.CharField(max_length=100, choices=dopuszczenie, default=EURO, blank=True, null=True)
    proof_of_ownership = models.FileField(blank=True, null=True)


class VehDeregister(models.Model):
    vehicle_id = models.CharField(max_length=10, blank=True, null=True)
    reason = models.CharField(max_length=250, blank=True, null=True)
    proof_of_ownership = models.FileField(blank=True, null=True)
