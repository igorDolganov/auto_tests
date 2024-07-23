"""методы проверки запросов"""
from requests import Response


class Check:

    """метод проверки статус кода"""

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code, f"ERROR, status code: {response.status_code}"
