from django.contrib import admin

from salons.models import Salon


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    pass
