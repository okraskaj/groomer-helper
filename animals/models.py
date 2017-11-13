from django.db import models

from breeds.models import Breed
from owners.models import Owner


class Animal(models.Model):
    GENDER_CHOICES = [
        (True, 'Male'),
        (False, 'Female'),
    ]

    name = models.TextField(max_length=100, blank=True, null=True)
    gender = models.BooleanField(choices=GENDER_CHOICES)
    breed = models.ForeignKey(Breed)
    color = models.TextField(max_length=50, blank=True, null=True)
    # service -dopytać
    photo = models.ImageField()
    notes = models.TextField(max_length=200, blank=True, null=True)
    owner = models.ForeignKey(Owner)
