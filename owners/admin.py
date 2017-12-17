from django.contrib import admin

from owners.models import Owner


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    pass
