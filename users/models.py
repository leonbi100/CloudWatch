from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    address = models.CharField(max_length=255, null=False, blank=False, unique=True)

    def __str__(self):
        return self.email