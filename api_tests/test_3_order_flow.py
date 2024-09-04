import requests
import config
import time
import allure


@allure.title("Начало аренды")
def test_make_order(base_url):
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json-patch+json',
        'Authorization': f'Bearer {config.access_token}',
    }

    json_data = {"identifier": config.StationIdentifier,
                 "locationLat": config.locationLat,
                 "locationLng": config.locationLng,
                 "isQrCode": True,
                 "referral": ""}

    response = requests.post(f'{base_url}/ordering-powerbank/api/Orders/make', headers=headers,
                             json=json_data)
    response_body = response.json()
    config.activity_id = response_body['activity']['id']

    assert response.status_code == 200
    assert len(response_body['activity']['id']) == 24
    time.sleep(5)


@allure.title("Проверка наличия аренды")
def test_check_activity(base_url):
    headers = {
        'Authorization': f'Bearer {config.access_token}',
    }

    response = requests.get(f'{base_url}/gatewayclient/api/powerbank/v1/activity', headers=headers)
    response_body = response.json()
    config.powerBankIdentifier = response_body['activities'][0]['powerBankIdentifier']
    print(f"Номер павербанка {config.powerBankIdentifier}")
    assert response.status_code == 200
    # Так как на данный момент не доступна мульти аренда, то мы достаем первую активити из списка
    assert response_body['activities'][0]['id'] == config.activity_id
    assert response_body['activities'][0]["status"] == "Ordered"
    # Убрать индексы, добавить проверку циклом


@allure.title("Завершение аренды")
def test_end_order(base_url):
    headers = {
        'content-type': "application/json; charset=utf-8"
    }
    # Получаем список эмуляторов
    response = requests.get(f'{base_url}/emulatorgetenergy/api/emulator')
    stations_list = response.json()['entries']

    # Перебираем все эмуляторы, находим эмулятор с StationIdentifier нашей станции, сохраняем его ID в
    # station_ID_by_StationIdentifier
    station_ID_by_StationIdentifier = None
    station_info_json = None
    for station in stations_list:
        if int(station['stationShortCode']) == int(config.StationIdentifier):
            station_ID_by_StationIdentifier = station['id']

            # Перебираем слоты в нашем эмуляторе, находим пустой
            slots_list = station['batteries']
            for slot in slots_list:
                if slot['value'] == "":
                    # Подменяем значение в пустом слоте на Identifier повербанка из аренды
                    # Раскодируем diceceID
                    print()
                    print(config.powerBankIdentifier)
                    print(config.powerBankIdentifier[0:4])
                    print(config.powerBankIdentifier[0:4].encode("ASCII").hex())
                    print(config.powerBankIdentifier[4:])
                    decoded_pb_id = config.powerBankIdentifier[0:4].encode("ASCII").hex().upper() + config.powerBankIdentifier[4:]
                    slot['value'] = decoded_pb_id
                    # Сделать отдельную функцию на конвертацию.
                    # Сохраняем информацию о станции с подмененным повербанком в json с инфой по станции. Далее
                    # используем это json для запроса на завершение аренды
                    station_info_json = station
                    break
            break

    # Отправляем запрос /emulator/[ID], подставляем в него номер нашего PowrbankIdenifier — Аренда завершается
    response = requests.post(
        f'{base_url}/emulatorgetenergy/api/emulator/{station_ID_by_StationIdentifier}', json=station_info_json, headers=headers)

    assert response.status_code == 200
    time.sleep(5)


@allure.title("Проверка окончания аренды")
def test_null_activity(base_url):
    headers = {
        'Authorization': f'Bearer {config.access_token}',
    }

    response = requests.get(f'{base_url}/gatewayclient/api/powerbank/v1/activity', headers=headers)
    response_body = response.json()
    assert response.status_code == 200
    assert len(response_body['activities']) == 0
    assert response_body['succeeded']


