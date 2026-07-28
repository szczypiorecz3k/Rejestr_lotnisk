import pytest

from .models.aerodrome import Aerodrome


@pytest.mark.django_db
def test_get_aerodromes(client):
    Aerodrome.objects.create(
        icao_code='EPWA',
        name='Port Lotniczy Warszawa-Okęcie im.Fryderyka Chopina',
        city='Warszawa',
    )
    response = client.get('/api/aerodrome/')

    assert response.status_code == 200

    data = response.json()
    assert len(data) == 1
    assert data[0]['icao_code'] == 'EPWA'
    assert data[0]['name'] == 'Port Lotniczy Warszawa-Okęcie im.Fryderyka Chopina'
    assert data[0]['city'] == 'Warszawa'


@pytest.mark.django_db
def test_get_aerodrome_by_icao_code(client):
    Aerodrome.objects.create(
        icao_code='EPWA',
        name='Port Lotniczy Warszawa-Okęcie im.Fryderyka Chopina',
        city='Warszawa',
    )

    response = client.get('/api/aerodrome/EPWA')

    assert response.status_code == 200
    data = response.json()
    assert data['icao_code'] == 'EPWA'


@pytest.mark.django_db
def test_get_non_existing_aerodrome_by_icao_code(client):
    Aerodrome.objects.create(
        icao_code='EPWA',
        name='Port Lotniczy Warszawa-Okęcie im.Fryderyka Chopina',
        city='Warszawa',
    )

    response = client.get('/api/aerodrome/XXXX')

    assert response.status_code == 404
