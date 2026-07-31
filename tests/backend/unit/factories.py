from unittest.mock import Mock

import pytest

from aerodrome.models.aerodrome import Aerodrome
from aerodrome.models.runway import Runway
import factory


class AerodromeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Aerodrome

    icao_code = factory.Faker('bothify', text='EP??')
    name = factory.Sequence(lambda x: f'name {x:02d}')
    city = factory.Sequence(lambda x: f'city {x:02d}')


class RunwayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Runway

    len = 3000
    code = '11'
    aerodrome = factory.SubFactory(AerodromeFactory)
