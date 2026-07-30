import pytest
from django.core.exceptions import ValidationError
from django.db.utils import DataError, IntegrityError

from aerodrome.models.aerodrome import Aerodrome
from aerodrome.models.runway import Runway


@pytest.mark.django_db
def test_add_len_too_short_runway():
    runway = Runway.objects.create(len=2, code='22L', aerodrome=create_aerodrome('epwa'))

    with pytest.raises(ValidationError):
        runway.full_clean()


@pytest.mark.django_db
def test_add_code_too_long_runway():
    with pytest.raises(DataError):
        runway = Runway.objects.create(len=200, code='222L', aerodrome=create_aerodrome('epwa'))
        runway.full_clean()


@pytest.mark.django_db
def test_add_aerodrome_and_code_not_unique_runway():
    aerodrome = create_aerodrome('epwa')
    Runway.objects.create(len=2, code='22L', aerodrome=aerodrome)
    with pytest.raises(IntegrityError):
        Runway.objects.create(len=2, code='22L', aerodrome=aerodrome)


@pytest.mark.django_db
def create_aerodrome(icao_code):
    return Aerodrome.objects.create(icao_code=icao_code, name='name', city='city')
