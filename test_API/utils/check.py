"""методы проверки запросов"""
import json

from requests import Response


class Check:

    """метод проверки статус кода"""

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code, f"ERROR, status code: {response.status_code}"

    """метод проверки наличия данных в ответе"""

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value, f"ERROR, field is not match"

    """метод проверки наличия текста в ответе"""
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, f"ERROR, value is not match"
