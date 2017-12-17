from django.db import models


class Breed(models.Model):
    SIZE_CHOICES = [
        ('miniature', 'Miniature'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        ('giant', 'Giant'),
    ]

    name = models.TextField(max_length=100, blank=False, null=False, unique=True)
    species = models.TextField(max_length=50, blank=False, default='dog')
    size = models.TextField(max_length=20, blank=True, choices=SIZE_CHOICES)
    grooming_notes = models.TextField(max_length=50, blank=True, null=False)
    hair_type = models.TextField(max_length=50, blank=True, null=False)
    # waga
    # photo
    # preferowane fryzury -> jedno lub wiecej zdjecie

    def __str__(self):
        return "".join([self.name, " - ", self.species])
