from django.contrib import admin

from .models.aerodrome import Aerodrome


@admin.register(Aerodrome)
class AerodromeAdmin(admin.ModelAdmin):
    list_display = (
        'icao_code',
        'name',
        'city',
    )
