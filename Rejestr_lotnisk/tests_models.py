import pytest
from django.core.exceptions import ValidationError
from django.db.utils import DataError, IntegrityError

from Rejestr_lotnisk.models import Aerodrome


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
        Aerodrome.objects.create(icao_code='EPWA', name='Port 2', city='Warszawa')


@pytest.mark.django_db
def test_str_returns_icao_code():
    aerodrome = Aerodrome.objects.create(icao_code='EPWA', name='Port 1', city='Warszawa')

    assert str(aerodrome) == aerodrome.icao_code


@pytest.mark.django_db
def test_icao_code_too_long():
    with pytest.raises(DataError):
        Aerodrome.objects.create(icao_code='EPWABC', name='Port', city='Warszawa')


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
