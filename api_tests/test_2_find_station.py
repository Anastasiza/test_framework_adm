import pytest
import requests
import config
import allure


@allure.title("Получение паверстанций в радиусе")
def test_stations_radius(base_url):
    headers = {
        'Authorization': f'Bearer {config.access_token}'

    }

    params = {
        'latitude': config.locationLat,
        'longitude': config.locationLng,
        'radiusbymeters': '500',
    }

    response = requests.get(f'{base_url}/gatewayclient/api/powerbank/v1/stations', params=params,
                            headers=headers)
    response_body = response.json()

    assert response.status_code == 200
    assert len(response_body["stations"]) > 0


@allure.title("Получение информации о станции по StationId")
def test_station_identifier(base_url):
    headers = {
        'Authorization': f'Bearer {config.access_token}',
    }

    params = {
        'identifier': str(config.StationIdentifier),
    }

    response = requests.get(f'{base_url}/gatewayclient/api/powerbank/v1/station', params=params,
                            headers=headers)
    response_body = response.json()
# Достать данные из ручки по радиусу и использовать их
    assert response.status_code == 200
    assert response_body['data']["stationId"]
    assert response_body['data']["shortCode"]
    assert response_body['data']["isOnline"]
    assert response_body['data']["working"]


@pytest.mark.parametrize("station_shortcode", config.shortcode)
@allure.title("Получение информации о станции по шоткоду")
def test_station_shortcode(base_url, station_shortcode):
    headers = {
        'Authorization': f'Bearer {config.access_token}',
    }

    params = {
        'identifier': station_shortcode,
    }

    response = requests.get(f'{base_url}/gatewayclient/api/powerbank/v1/station', params=params,
                            headers=headers)
    response_body = response.json()
    # Достать данные из ручки получение станции по айдентифаеру и использовать их
    assert response.status_code == 200
    assert response_body['data']["stationId"]
    assert response_body['data']["shortCode"]
    assert response_body['data']["isOnline"]
    assert response_body['data']["working"]


@allure.title("Получение информации о станции по QR-коду")
def test_station_qr_code(base_url):
    headers = {
        'Authorization': f'Bearer {config.access_token}',
    }

    params = {
        'identifier': f'{config.qr_code_string}{config.StationIdentifier}',
    }

    response = requests.get(f'{base_url}/gatewayclient/api/powerbank/v1/station', params=params,
                            headers=headers)
    response_body = response.json()
#Можно добавить цикл с проверками
    assert response.status_code == 200
    assert response_body['data']["stationId"]
    assert response_body['data']["shortCode"]
    assert response_body['data']["isOnline"]
    assert response_body['data']["working"]