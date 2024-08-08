import allure
import requests


"""Список HTTP методов"""


class HttpMethods:
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'identity'}
    headers_out = {'accept': '*/*'}
    cookie = ''

    @staticmethod
    def get(url):
        with allure.step('GET'):
            result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            return result

    @staticmethod
    def post(url, payload):
        with allure.step('POST'):
            result = requests.post(url, json=payload, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            return result

    @staticmethod
    def put(url, payload):
        with allure.step('PUT'):
            result = requests.put(url, json=payload, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            return result

    @staticmethod
    def delete(url, payload):
        with allure.step('DELETE'):
            result = requests.delete(url, json=payload, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            return result
