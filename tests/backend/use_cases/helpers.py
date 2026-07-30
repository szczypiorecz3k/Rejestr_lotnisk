import pytest

from aerodrome.repositories.aerodrome_repository import AerodromeRepository
from aerodrome.use_cases.add_aerodrome_use_case import AddAerodromeInputDto, AddAerodromeUseCase
from aerodrome.use_cases.delete_aerodrome_use_case import DeleteAerodromeUseCase


@pytest.fixture
def aerodrome_dto():
    return AddAerodromeInputDto(
        icao_code='EPWA',
        name='Port Lotniczy Warszawa-Okęcie im.Fryderyka Chopina',
        city='Warszawa',
    )


@pytest.fixture
def add_aerodrome_use_case():
    return AddAerodromeUseCase(AerodromeRepository())


@pytest.fixture
def delete_aerodrome_use_case():
    return DeleteAerodromeUseCase(AerodromeRepository())
