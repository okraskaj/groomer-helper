from django.contrib import admin

from animals.models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass
