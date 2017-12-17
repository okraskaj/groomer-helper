from django.contrib import admin
from breeds.models import Breed

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass
