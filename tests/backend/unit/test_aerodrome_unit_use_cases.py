from unittest.mock import Mock

import pytest

from aerodrome.use_cases.add_aerodrome_use_case import AddAerodromeInputDto, AddAerodromeUseCase
from aerodrome.use_cases.delete_aerodrome_use_case import DeleteAerodromeUseCase
from event_bus.event_bus import event_bus


@pytest.fixture
def aerodrome_dto():
    return AddAerodromeInputDto(
        icao_code='EPWA',
        name='Port Lotniczy Warszawa-Okęcie im.Fryderyka Chopina',
        city='Warszawa',
    )


@pytest.fixture
def aerodrome_repository():
    repo = Mock()
    repo.create.return_value = Mock(icao_code='EPWA')
    return repo


@pytest.fixture
def add_aerodrome_use_case(aerodrome_repository):
    return AddAerodromeUseCase(aerodrome_repository=aerodrome_repository)


@pytest.fixture
def delete_aeroddrome_use_case(aerodrome_repository):
    return DeleteAerodromeUseCase(aerodrome_repository=aerodrome_repository)


@pytest.fixture
def publish_mock(monkeypatch):
    mock = Mock()

    monkeypatch.setattr(
        event_bus,
        'publish',
        mock,
    )
    return mock


@pytest.mark.django_db
def test_add_aerodrome_use_case_calls_repository(
    aerodrome_dto, add_aerodrome_use_case, aerodrome_repository
):
    add_aerodrome_use_case.execute(aerodrome_dto)

    aerodrome_repository.create.assert_called_once_with(
        icao_code='EPWA',
        name='Port Lotniczy Warszawa-Okęcie im.Fryderyka Chopina',
        city='Warszawa',
    )


@pytest.mark.django_db
def test_delete_aerodrome_use_case_calls_repository(
    aerodrome_repository, delete_aeroddrome_use_case
):
    delete_aeroddrome_use_case.execute('EPWA')

    aerodrome_repository.delete.assert_called_once_with('EPWA')


@pytest.mark.django_db
def test_create_aerodrome_use_case_emits_event(publish_mock, aerodrome_dto, add_aerodrome_use_case):
    add_aerodrome_use_case.execute(aerodrome_dto)

    publish_mock.assert_called_once()


@pytest.mark.django_db
def test_delete_aerodrome_use_case_emits_event(delete_aeroddrome_use_case, publish_mock):
    delete_aeroddrome_use_case.execute('EPWA')

    publish_mock.assert_called_once()
