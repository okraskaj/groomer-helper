from datetime import datetime

from django.db import models
from django.db.models import Max
from django.urls import reverse

from breeds.models import Breed
from owners.models import Owner


class Animal(models.Model):
    GENDER_CHOICES = [
        (True, 'Male'),
        (False, 'Female'),
    ]

    name = models.TextField(max_length=100, blank=True, null=True)
    gender = models.BooleanField(choices=GENDER_CHOICES)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    color = models.TextField(max_length=100, blank=True, null=True)
    photo = models.ImageField()
    notes = models.TextField(max_length=200, blank=True, null=True)
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
    )

    def gender_verbose(self):
        return dict(Animal.GENDER_CHOICES)[self.gender]

    def get_last_visit(self):
        return self.visit_set.filter(start__lt=datetime.now()).latest('start').start

    def get_next_visit(self):
        return self.visit_set.filter(start__gt=datetime.now()).earliest('start').start

    def get_absolute_url(self):
        return reverse('animal-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "".join([self.name, " - ", self.breed.species, " rasy ", self.breed.name])
