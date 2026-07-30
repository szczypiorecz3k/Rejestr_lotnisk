import pytest
from aerodrome.use_cases.delete_aerodrome_use_case import DeleteAerodromeUseCase
from aerodrome.use_cases.add_aerodrome_use_case import AddAerodromeUseCase, AddAerodromeInputDto
from aerodrome.models import Aerodrome
from aerodrome.repositories.aerodrome_repository import AerodromeRepository
from aerodrome.models.aerodrome_stats import AerodromeStats
from aerodrome.exceptions import AerodromeNotExistError


@pytest.fixture
def valid_dto():
    return AddAerodromeInputDto(
        icao_code='EPWA',
        name='Port Lotniczy Warszawa-Okęcie im.Fryderyka Chopina',
        city='Warszawa',)


@pytest.fixture
def add_use_case():
    return AddAerodromeUseCase(AerodromeRepository())


@pytest.fixture
def delete_use_case():
    return DeleteAerodromeUseCase(AerodromeRepository())


@pytest.mark.django_db
def test_add_valid_Aerodrome(valid_dto, add_use_case):
    add_use_case.execute(valid_dto)

    assert Aerodrome.objects.filter(icao_code='EPWA').exists()
    db_aerodrome = Aerodrome.objects.get(icao_code='EPWA')
    assert db_aerodrome.name == 'Port Lotniczy Warszawa-Okęcie im.Fryderyka Chopina'
    assert db_aerodrome.city == 'Warszawa'


@pytest.mark.django_db
def test_delete_existing_aerodrome_and_check_stats(valid_dto, add_use_case, delete_use_case):
    add_use_case.execute(valid_dto)

    delete_use_case.execute(icao_code=valid_dto.icao_code)

    with pytest.raises(Aerodrome.DoesNotExist):
        Aerodrome.objects.get(icao_code=valid_dto.icao_code)
    assert not AerodromeStats.objects.first().total


@pytest.mark.django_db
def test_delete_non_existing_aerodrome_and_check_stats(delete_use_case):
    with pytest.raises(AerodromeNotExistError):
        delete_use_case.execute(icao_code='xxxx')

    assert not AerodromeStats.objects.count()


@pytest.mark.django_db
def test_add_aerodrome_and_check_stats(valid_dto, add_use_case):
    add_use_case.execute(valid_dto)

    assert AerodromeStats.objects.first().total == 1
