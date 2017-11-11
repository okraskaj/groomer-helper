from django.db import models


class Owner(models.Model):
    full_name = models.TextField(max_length=100, blank=True, null=True)
    phone_number = models.TextField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=True, null=True)
    location = models.TextField(max_length=200, blank=True, null=True)
    recommended_by = models.ManyToManyField('self', symmetrical=False)
    #field to reward people with most recomendations as well as to remember people correctly
    # TODO: integrate with facebook - load image picture on creation and load additional data (likes?).
