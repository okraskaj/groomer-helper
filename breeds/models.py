from django.db import models


class Breed(models.Model):
    SIZE_CHOICES = [
        ('miniature', 'Miniature'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        ('giant', 'Giant'),
    ]
    SPECIES_CHOICES = [
        ('pies', 'Pies'),
        ('kot', 'Kot'),
        ('świnka morska', 'Świnka morska'),
        ('królik', 'Królik'),
    ]

    HAIR_TYPE_CHOICES = [
        ('normalna', 'Normalna'),
        ('szorstka', 'Szorstka'),
        ('miękka', 'Miękka'),
        ('duża ilość podszerstka', 'Duża ilość podszerstka'),
        ('twarda', 'Twarda')
    ]

    name = models.TextField(max_length=100, blank=False, null=False, unique=True)
    species = models.TextField(max_length=50, blank=False, default='dog')
    size = models.TextField(max_length=20, blank=True, choices=SIZE_CHOICES)
    grooming_notes = models.TextField(max_length=50, blank=True, null=False)
    hair_type = models.TextField(max_length=50, blank=True, null=False)
    weight = models.IntegerField(default=20, blank=False, null=False)
    photo = models.ImageField(upload_to='breed-avatars/', default='breed-avatars/None/no-img.png')

    # TODO: preferowane fryzury -> jedno lub wiecej zdjecie

    def __str__(self):
        return "".join([self.name, " - ", self.species])
