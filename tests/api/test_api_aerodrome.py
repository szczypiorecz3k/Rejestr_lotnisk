import pytest

from aerodrome.models.aerodrome import Aerodrome
from aerodrome.models.aerodrome_stats import AerodromeStats
from aerodrome.models.runway import Runway
from aerodrome.use_cases.add_aerodrome_use_case import AddAerodromeInputDto, CreateRunwayInputDto, AddAerodromeWithRunwaysInputDto


@pytest.fixture
def aerodrome_dto():
    return AddAerodromeInputDto(
        icao_code='EPWA',
        name='Port Lotniczy Warszawa-Okęcie im.Fryderyka Chopina',
        city='Warszawa',
    )


@pytest.fixture
def runway_dto():
    return CreateRunwayInputDto(
        len=200,
        code='12L',
    )


@pytest.fixture
def aerodrome_with_runways_dto(aerodrome_dto, runway_dto):
    return AddAerodromeWithRunwaysInputDto(icao_code=aerodrome_dto.icao_code,
                                           name=aerodrome_dto.name,
                                           city=aerodrome_dto.city,
                                           runways=[runway_dto])


def aerodrome_create(aerodrome_dto):
    return Aerodrome.objects.create(icao_code=aerodrome_dto.icao_code,
                                    name=aerodrome_dto.name,
                                    city=aerodrome_dto.city)


@pytest.mark.django_db
def test_get_aerodromes(client, aerodrome_dto):
    aerodrome_create(aerodrome_dto)
    response = client.get('/api/aerodrome/')

    assert response.status_code == 200

    data = response.json()
    assert len(data) == 1
    assert data[0]['icao_code'] == 'EPWA'
    assert data[0]['name'] == 'Port Lotniczy Warszawa-Okęcie im.Fryderyka Chopina'
    assert data[0]['city'] == 'Warszawa'


@pytest.mark.django_db
def test_get_aerodrome_by_icao_code(client, aerodrome_dto):
    aerodrome_create(aerodrome_dto)

    response = client.get('/api/aerodrome/EPWA')

    assert response.status_code == 200
    data = response.json()
    assert data['icao_code'] == 'EPWA'


@pytest.mark.django_db
def test_get_non_existing_aerodrome_by_icao_code(client, aerodrome_dto):
    aerodrome_create(aerodrome_dto)

    response = client.get('/api/aerodrome/XXXX')

    assert response.status_code == 404


@pytest.mark.django_db
def test_post_aerodrome_with_runways(client, aerodrome_with_runways_dto):
    response = client.post(
        '/api/aerodrome/', aerodrome_with_runways_dto.model_dump(mode='json'),
        content_type='application/json')
    assert response.status_code == 200
    assert Aerodrome.objects.filter(icao_code='EPWA').exists()
    assert Runway.objects.filter(code='12L').exists()
    assert response.json() == 'Aerodrome created'


@pytest.mark.django_db
def test_delete_aerodrome(client, aerodrome_dto):
    aerodrome_create(aerodrome_dto)
    response = client.delete('/api/aerodrome/EPWA')

    assert response.status_code == 200
    assert not Aerodrome.objects.filter(icao_code='EPWA').exists()
    print(response.json())
    assert response.json() == 'Aerodrome deleted'


@pytest.mark.django_db
def test_delete_non_existing_aerodrome(client):
    response = client.delete('/api/aerodrome/EPWA')
    print(response.json())
    assert response.status_code == 404
    assert response.json()['detail'] == 'Aerodrome not found'


@pytest.mark.django_db
def test_get_aerodrome_count(client):
    AerodromeStats.objects.create()

    response = client.get('/api/aerodrome/total')

    assert response.status_code == 200
    assert response.json() == 0
