import pytest

from aerodrome.exceptions import AerodromeNotExistError
from aerodrome.models import Aerodrome
from aerodrome.models.aerodrome_stats import AerodromeStats


@pytest.mark.django_db
def test_add_valid_Aerodrome(aerodrome_dto, add_aerodrome_use_case):
    add_aerodrome_use_case.execute(aerodrome_dto)

    assert Aerodrome.objects.filter(icao_code='EPWA').exists()
    db_aerodrome = Aerodrome.objects.get(icao_code='EPWA')
    assert db_aerodrome.name == 'Port Lotniczy Warszawa-Okęcie im.Fryderyka Chopina'
    assert db_aerodrome.city == 'Warszawa'


@pytest.mark.django_db
def test_delete_existing_aerodrome_and_check_stats(
    aerodrome_dto, add_aerodrome_use_case, delete_aerodrome_use_case
):
    add_aerodrome_use_case.execute(aerodrome_dto)

    delete_aerodrome_use_case.execute(icao_code=aerodrome_dto.icao_code)

    with pytest.raises(Aerodrome.DoesNotExist):
        Aerodrome.objects.get(icao_code=aerodrome_dto.icao_code)
    assert not AerodromeStats.objects.first().total


@pytest.mark.django_db
def test_delete_non_existing_aerodrome_and_check_stats(delete_aerodrome_use_case):
    with pytest.raises(AerodromeNotExistError):
        delete_aerodrome_use_case.execute(icao_code='xxxx')

    # deleting non existng aerodrome should not emmit stats update event
    assert not AerodromeStats.objects.count()


@pytest.mark.django_db
def test_add_aerodrome_and_check_stats(aerodrome_dto, add_aerodrome_use_case):
    add_aerodrome_use_case.execute(aerodrome_dto)

    assert AerodromeStats.objects.first().total == 1
