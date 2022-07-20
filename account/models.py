from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    class Types(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        VICE_PRINCIPAL = "VICE PRINCIPAL", "VICE PRINCIPAL"
        ACCOUNTANT = "ACCOUNTANT", "ACCOUNTANT"
    GENDER_CHOICES = (('Male','Male'), ('Female', 'Female'))
    type = models.CharField(_("Type"), max_length=50, choices=Types.choices, default=Types.ACCOUNTANT)
    gender = gender = models.CharField(max_length=10, null=True, choices=GENDER_CHOICES)
    phone_number = PhoneNumberField(null=True)
    other_name = models.CharField(max_length=20, null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=255, null=True)
    profile_pic = models.ImageField(upload_to='Profile Picture', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
