import pytest
from django.core.exceptions import ValidationError
from django.db.utils import DataError, IntegrityError
from aerodrome.use_cases.delete_aerodrome_use_case import DeleteAerodromeUseCase
from aerodrome.use_cases.add_aerodrome_use_case import AddAerodromeUseCase, AddAerodromeInputDto
from aerodrome.models import Aerodrome
from aerodrome.repositories.aerodrome_repository import AerodromeRepository


@pytest.mark.django_db  # czy zawsze uzywam tego dekoratora?
def test_create_valid_Aerodrome():
    aerodrome_valid = Aerodrome.objects.create(
        icao_code='EPWA',
        name='Port Lotniczy Warszawa-Okęcie im.Fryderyka Chopina',
        city='Warszawa',
    )

    assert aerodrome_valid.icao_code == 'EPWA'
    assert aerodrome_valid.name == 'Port Lotniczy Warszawa-Okęcie im.Fryderyka Chopina'
    assert aerodrome_valid.city == 'Warszawa'


@pytest.mark.django_db
def test_icao_code_must_be_unique():
    Aerodrome.objects.create(icao_code='EPWA', name='Port 1', city='Warszawa')

    with pytest.raises(IntegrityError):
        Aerodrome.objects.create(
            icao_code='EPWA', name='Port 2', city='Warszawa')


@pytest.mark.django_db
def test_str_returns_icao_code():
    aerodrome = Aerodrome.objects.create(
        icao_code='EPWA', name='Port 1', city='Warszawa')

    assert str(aerodrome) == aerodrome.icao_code


@pytest.mark.django_db
def test_icao_code_too_long():
    with pytest.raises(DataError):
        Aerodrome.objects.create(
            icao_code='EPWABC', name='Port', city='Warszawa')


@pytest.mark.django_db
def test_icao_code_too_short():
    aerodrome_too_short_icao_code = Aerodrome.objects.create(
        icao_code='EP', name='Port', city='Warszawa'
    )

    with pytest.raises(ValidationError):
        aerodrome_too_short_icao_code.full_clean()


@pytest.mark.django_db
def test_icao_code_must_be_all_letters():
    aerodrome_with_numbers = Aerodrome.objects.create(
        icao_code='EPw1', name='Port', city='Warszawa'
    )
    with pytest.raises(ValidationError):
        aerodrome_with_numbers.full_clean()


@pytest.mark.django_db
def test_icao_code_can_be_written_lowercase():
    aerodrome_icao_in_lowercase = Aerodrome.objects.create(
        icao_code='epwa', name='Port', city='Warszawa'
    )
    assert aerodrome_icao_in_lowercase.icao_code == 'EPWA'


@pytest.mark.django_db
def test_delete_existing_aerodrome_and_check_stats():
    aerodrome = AddAerodromeInputDto(
        icao_code='epwa',
        name='Port Lotniczy Warszawa-Okęcie im.Fryderyka Chopina',
        city='Warszawa',)
    add_use_case = AddAerodromeUseCase(AerodromeRepository())
    add_use_case.execute(aerodrome)

    delete_use_case = DeleteAerodromeUseCase(AerodromeRepository())
    delete_use_case.execute(icao_code='epwa')

    with pytest.raises(Aerodrome.DoesNotExist):
        Aerodrome.objects.get(icao_code='epwa')


'''
test_delete_non_existing_aerodrome_and_check_stats()
'''
