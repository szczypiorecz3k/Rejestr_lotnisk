from unittest.mock import Mock

import pytest

from aerodrome.repositories.aerodrome_repository import AerodromeRepository
from aerodrome.use_cases.add_runway_use_case import AddRunwayInputDto, AddRunwayUseCase
from tests.backend.unit.helpers import aerodrome_dto, add_aerodrome_use_case, aerodrome_repository


@pytest.fixture
def runway_dto():
    return AddRunwayInputDto(len=1000, code='12L', aerodrome_icao_code='EPWA')


@pytest.fixture
def runway_repository():
    return Mock()


@pytest.fixture
def add_runway_use_case(runway_repository):
    return AddRunwayUseCase(runway_repository=runway_repository)


@pytest.fixture(autouse=True)
def aerodrome_get_by_icao_code_mock(monkeypatch):
    mock = Mock()
    mock.get_by_icao_code.return_value = Mock(icao_code='EPWA')

    monkeypatch.setattr(
        AerodromeRepository,
        'get_by_icao_code',
        mock,
    )
    return mock


@pytest.mark.django_db
def test_add_runway_use_case_calls_repository(
    runway_dto, runway_repository, add_runway_use_case, aerodrome_dto, add_aerodrome_use_case
):
    add_aerodrome_use_case.execute(aerodrome_dto)
    add_runway_use_case.execute(runway_dto)

    runway_repository.create.assert_called_once()
