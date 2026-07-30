from unittest.mock import Mock

import pytest

from aerodrome.use_cases.add_runway_use_case import AddRunwayInputDto, AddRunwayUseCase


@pytest.fixture
def runway_dto():
    return AddRunwayInputDto(len=1000, code='12L', aerodrome_icao_code='EPWA')


@pytest.fixture
def runway_repository():
    return Mock()


@pytest.fixture
def add_runway_use_case(runway_repository):
    return AddRunwayUseCase(runway_repository=runway_repository)


@pytest.mark.django_db
def test_add_runway_use_case_calls_repository(
    runway_dto, runway_repository, add_runway_use_case, aerodrome_dto, add_aerodrome_use_case
):
    add_aerodrome_use_case.execute(aerodrome_dto)
    add_runway_use_case.execute(runway_dto)

    runway_repository.create.assert_called_once()


def test_add_runway_with_non_existing_aerodrome_use_case_raises_exception():
    pass
