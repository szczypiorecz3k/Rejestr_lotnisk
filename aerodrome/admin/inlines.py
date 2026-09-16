from django.contrib import admin

from aerodrome.models.runway import Runway


class RunwayInline(admin.StackedInline):
    model = Runway
    fields = ('aerodrome', 'length', 'code',)
