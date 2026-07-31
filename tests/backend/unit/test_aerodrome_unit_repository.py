
from unittest.mock import Mock

from aerodrome.models.aerodrome import Aerodrome
from aerodrome.repositories.aerodrome_repository import AerodromeRepository
from tests.backend.unit.factories import AerodromeFactory


def test_get_by_icao_code():
    aerodrome = AerodromeFactory.build(icao_code="EPWA")

    Aerodrome.objects.get = Mock(return_value=aerodrome)

    result = AerodromeRepository.get_by_icao_code("EPWA")

    assert result == aerodrome


def test_get_by_city():
    aerodromes_w = AerodromeFactory.build_batch(2)
    aerodrome_p = AerodromeFactory.build(city='Poznan')

    Aerodrome.objects.filter = Mock(return_value=aerodromes_w)

    result = AerodromeRepository.get_by_city('Warszawa')
    assert result == aerodromes_w
