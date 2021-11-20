from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    class Role(models.TextChoices):
        PETITIONER = 'petitioner',
        CLERK = 'clerk'

    role = models.CharField(
        max_length=21,
        choices=Role.choices,
        default=Role.PETITIONER,
    )
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
