import requests
import config
import allure
from pprint import pprint
import time


class TestAuthorization:

    @allure.title("Получение смс-кода")
    def test_sms_code(self, base_url):
        headers = {
            'Content-Type': 'application/json',
        }

        json_data = {
            'UniqueId': '6A1A1405-1C14-47A7-9703-A54A48B98413',
            'PhoneModel': 'iPhone11,3',
            'osVersion': '16.0.0',
            'PhoneNumber': f'{config.PhoneNumber}'
        }

        response = requests.post(f'{base_url}/gatewayclient/api/v1/mobile/code', headers=headers,
                                 json=json_data)
        response_body = response.json()
        assert response.status_code == 200
        assert response_body["result"] == "SmsCodeSent"

    @allure.title("Получение токена")
    def test_token(self, base_url):
        data = {
            'client_id': config.client_id,
            'client_secret': config.client_secret,
            'grant_type': 'password',
            'username': config.PhoneNumber,
            'password': config.sms_code,
        }

        response = requests.post(f'{base_url}/gatewayclient/api/v1/connect/token', data=data)
        config.access_token = response.json()["access_token"]
        response_body = response.json()
        assert response.status_code == 200
        assert response_body["access_token"]
