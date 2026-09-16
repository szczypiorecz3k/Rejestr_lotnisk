from django.contrib import admin

from aerodrome.admin.forms import AerodromeAdminForm

from aerodrome.admin.inlines import RunwayInline
from aerodrome.models.aerodrome import Aerodrome
from aerodrome.models.runway import Runway


@admin.register(Aerodrome)
class AerodromeAdmin(admin.ModelAdmin):
    list_display = (
        'icao_code',
        'name',
        'city',
    )
    form = AerodromeAdminForm
    inlines = [RunwayInline]


@admin.register(Runway)
class RunwayAdmin(admin.ModelAdmin):
    list_display = ('length', 'code', 'aerodrome',)
    list_filter = ('aerodrome',)
    search_fields = ('aerodrome__code',)
