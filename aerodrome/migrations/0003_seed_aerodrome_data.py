import os
from django.db import migrations

from aerodrome.migrations.seed_data.aerodromes_data import AERODROMES
from aerodrome.migrations.seed_data.runways_data import RUNWAYS


def seed_aerodromes_with_runways(apps, schema_editor):
    print('jestem')
    Aerodrome = apps.get_model('aerodrome', 'Aerodrome')

    for aerodrome_data in AERODROMES:
        Aerodrome.objects.get_or_create(
            icao_code=aerodrome_data['code'],
            defaults={
                'name': aerodrome_data['name'],
                'city': aerodrome_data['city']
            },
        )

    Runway = apps.get_model('aerodrome', 'Runway')
    for runway_data in RUNWAYS:
        aerodrome = Aerodrome.objects.get(
            icao_code=runway_data['aerodrome_code'])

        Runway.objects.create(
            code=runway_data['runway_code'],
            aerodrome=aerodrome,
            length=runway_data['tora'],
        )


def reverse_seed_aerodromes_with_runways(apps, schema_editor):
    Aerodrome = apps.get_model('aerodrome', 'Aerodrome')
    aerodrome_codes = [aerodrome['code'] for aerodrome in AERODROMES]
    Aerodrome.objects.filter(icao_code__in=aerodrome_codes).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('aerodrome', '0002_aerodromestats_alter_aerodrome_icao_code_runway'),
    ]

    operations = [
        migrations.RunPython(
            seed_aerodromes_with_runways,
            reverse_seed_aerodromes_with_runways
        ),
    ]
