import os
from django.db import migrations

from aerodrome.migrations.seed_data.aerodromes_data import AERODROMES
from aerodrome.migrations.seed_data.runways_data import RUNWAYS


def seed_aerodromes_with_runways(apps, schema_editor):
    if os.getenv("PYTEST_CURRENT_TEST") or os.getenv("ENV_TYPE") != 'dev':
        return

    Aerodrome = apps.get_model('aerodrome', 'Aerodrome')

    # 1. Tworzenie lotnisk
    for aerodrome_data in AERODROMES:
        Aerodrome.objects.get_or_create(
            icao_code=aerodrome_data['code'],
            defaults={
                'name': aerodrome_data['name'],
                'city': aerodrome_data['city']
            },
        )

    # 2. Tworzenie pasów startowych
    Runway = apps.get_model('aerodrome', 'Runway')
    for runway_data in RUNWAYS:
        # Pobieramy lotnisko używając poprawnego pola icao_code oraz klucza ze słownika
        aerodrome = Aerodrome.objects.get(
            icao_code=runway_data['aerodrome_code'])

        Runway.objects.get_or_create(
            code=runway_data['runway_code'],
            aerodrome=aerodrome,
            defaults={
                'length': runway_data['tora']
            }
        )


def reverse_seed_aerodromes_with_runways(apps, schema_editor):
    Aerodrome = apps.get_model('aerodrome', 'Aerodrome')
    aerodrome_codes = [aerodrome['code'] for aerodrome in AERODROMES]
    Aerodrome.objects.filter(icao_code__in=aerodrome_codes).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('aerodrome', '0007_alter_aerodromestats_total_alter_runway_length'),
    ]

    operations = [
        migrations.RunPython(
            seed_aerodromes_with_runways,
            reverse_seed_aerodromes_with_runways
        ),
    ]
