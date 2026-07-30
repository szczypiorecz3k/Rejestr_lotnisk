from unittest.mock import Mock

import pytest
from aerodrome.models.aerodrome import Aerodrome
from aerodrome.models.runway import Runway
from aerodrome.use_cases.add_runway_use_case import AddRunwayInputDto, AddRunwayUseCase
from helpers import aerodrome_dto, add_aerodrome_use_case


@pytest.fixture
def runway_dto():
    aerodrome = Mock(spec=Aerodrome)
    aerodrome.icao_code = 'EPWA'
    return AddRunwayInputDto(len=1000, code='12L', aerodrome=aerodrome)


@pytest.fixture
def runway_repository():
    return Mock()


@pytest.fixture
def add_runway_use_case(runway_repository):
    return AddRunwayUseCase(runway_repository=runway_repository)


@pytest.mark.django_db
def test_add_runway_use_case_calls_repository(runway_dto, runway_repository):
    '''
    add_runway_use_case.execute(runway_dto)

    runway_repository.assert_called_once()
    '''


def test_add_runway_with_non_existing_aerodrome_use_case_raises_exception():
    pass
