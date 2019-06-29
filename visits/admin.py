from django.contrib import admin

from visits.models import Visit


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = (str, 'start', 'stop', 'animal')
