import os

from django.db import migrations

from aerodrome.migrations.seed_data.aerodromes_data import AERODROMES
from aerodrome.migrations.seed_data.runways_data import RUNWAYS



def seed_aerodromes_with_runways(apps, schema_editor):
    if os.getenv("PYTEST_CURRENT_TEST") or os.getenv("ENV_TYPE") != 'dev':
        return
    Aerodrome = apps.get_model('aerodrome', 'Aerodrome')

    for aerodrome_data in AERODROMES:
        aerodrome,_ = Aerodrome.objects.get_or_create(
            code=aerodrome_data['code'],
            defaults=aerodrome_data,
            )
        

    Runway = apps.get_model('aerodrome', 'Runway')
    for runway_data in RUNWAYS:
        aerodrome = Aerodrome.objects.get(code=runway_data['aerodrome_code'])

        Runway.objects.get_or_create(
            code=runway_data['runway_code'],
            aerodrome=aerodrome, 
            length=runway_data['tora'],
        )

    
def reverse_seed_aerodromes_with_runways(apps,schema_editor):
    Aerodrome = apps.get_model('aerodrome', 'Aerodrome')

    aerodrome_codes = [aerodrome['code'] for aerodrome in AERODROMES]
    Aerodrome.objects.filter(code__in=aerodrome_codes).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('aerodrome','0004_aerodrome_is_international_alter_aerodrome_subtype'),
        ('airac','0002_seed_initial_airac_cycle' ),
    ]

    operations = [
        migrations.RunPython(seed_aerodromes_with_runways,
                                      reverse_seed_aerodromes_with_runways),
    ]