from django.db import models


class Salon(models.Model):
    full_name = models.TextField(max_length=100, blank=True, null=True)
    phone_number = models.TextField(max_length=20, blank=False, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    location = models.TextField(max_length=200, blank=True, null=True)
    subscription_type = models.TextField(max_length=200, blank=True, null=True)
    photo = models.ImageField(upload_to='salons/', default='salons/None/no-img.png')