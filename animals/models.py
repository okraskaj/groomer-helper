from django.db import models

from owners.models import Owner

SIZE_CHOICES = [
    ('miniature', 'Miniature'),
    ('medium', 'Medium'),
    ('large', 'Large'),
    ('giant', 'Giant'),
]

GENDER_CHOICES = [
    (True, 'Male'),
    (False, 'Female'),
]


class Animal(models.Model):
    name = models.TextField(max_length=100, blank=True, null=True)
    gender = models.BooleanField(choices=GENDER_CHOICES)
    species = models.TextField(max_length=50, blank=False, default='dog')
    size = models.TextField(max_length=20, blank=True, choices=SIZE_CHOICES)
    breed = models.TextField(max_length=20, blank=False, null=False)  # TODO: foreign key to Breeds
    color = models.TextField(max_length=50, blank=True, null=True)
    # service -dopytać
    photo = models.ImageField()
    motes = models.TextField(max_length=200, blank=True, null=True)
    owner = models.ForeignKey(Owner)
