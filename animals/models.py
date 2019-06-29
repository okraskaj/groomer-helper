from datetime import datetime

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from breeds.models import Breed
from config.settings import DEFAULT_SALON_ID
from owners.models import Owner
from salons.models import Salon


class Animal(models.Model):
    GENDER_CHOICES = [
        (True, _('Male')),
        (False, _('Female')),
    ]

    name = models.TextField(max_length=100, blank=True,
                            null=True, verbose_name=_('name'))
    gender = models.BooleanField(choices=GENDER_CHOICES,
                                 verbose_name=_('gender'))
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE,
                              verbose_name=_('breed'))
    color = models.TextField(max_length=100, blank=True,
                             null=True, verbose_name=_('color'))
    photo = models.ImageField(upload_to='animal-avatars/',
                              default='animal-avatars/None/no-img.png',
                              verbose_name=_('photo'))
    notes = models.TextField(max_length=200, blank=True,
                             null=True, verbose_name=_('notes'))
    owner = models.ForeignKey(
        Owner,
        verbose_name=_('owner'),
        on_delete=models.CASCADE,
    )
    salon = models.ForeignKey(Salon, default=DEFAULT_SALON_ID,
                              null=False, on_delete=models.CASCADE)

    def gender_verbose(self):
        return dict(Animal.GENDER_CHOICES)[self.gender]

    def get_last_visit(self):
        return self.visit_set.filter(
            start__lt=datetime.now()).latest('start').start

    def get_next_visit(self):
        return self.visit_set.filter(
            start__gt=datetime.now()).earliest('start').start

    def get_absolute_url(self):
        return reverse('animal-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "".join([self.name, " - ", self.breed.species,
                        " rasy ", self.breed.name])
