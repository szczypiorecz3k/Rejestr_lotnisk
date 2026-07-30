import pytest

from aerodrome.exceptions import AerodromeNotExistError
from aerodrome.repositories.runway_repository import RunwayRepository
from aerodrome.use_cases.add_runway_use_case import AddRunwayInputDto, AddRunwayUseCase


@pytest.fixture
def runway_dto():
    return AddRunwayInputDto(len=1000, code='12L', aerodrome_icao_code='EPWA')


@pytest.fixture
def add_runway_use_case():
    return AddRunwayUseCase(runway_repository=RunwayRepository())


@pytest.mark.django_db
def test_add_valid_runway_use_case(
    runway_dto, add_runway_use_case, aerodrome_dto, add_aerodrome_use_case
):
    add_aerodrome_use_case.execute(aerodrome_dto)
    add_runway_use_case.execute(runway_dto)

    assert RunwayRepository.get_by_aerodrome_icao_code('EPWA').count() == 1


@pytest.mark.django_db
def test_add_aerodrome_does_not_exist_runway_use_case(runway_dto, add_runway_use_case):
    with pytest.raises(AerodromeNotExistError):
        add_runway_use_case.execute(runway_dto)


@pytest.mark.django_db
def test_aerodrome_on_delete_collapse_runways(
    runway_dto,
    add_runway_use_case,
    aerodrome_dto,
    add_aerodrome_use_case,
    delete_aerodrome_use_case,
):

    add_aerodrome_use_case.execute(aerodrome_dto)
    add_runway_use_case.execute(runway_dto)
    delete_aerodrome_use_case.execute('EPWA')

    assert not RunwayRepository.get_by_aerodrome_icao_code('EPWA').count()
