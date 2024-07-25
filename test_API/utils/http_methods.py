import allure
import requests
from utils.logger import *

"""Список HTTP методов"""


class HttpMethods:
    headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'identity'}
    headers_out = {'accept': '*/*'}
    cookie = ''

    @staticmethod
    def get(url):
        with allure.step('GET'):
            Logger.add_request(url, method='GET')
            result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, payload):
        with allure.step('POST'):
            Logger.add_request(url, method='POST')
            result = requests.post(url, json=payload, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, payload):
        with allure.step('PUT'):
            Logger.add_request(url, method='PUT')
            result = requests.put(url, json=payload, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, payload):
        with allure.step('DELETE'):
            Logger.add_request(url, method='DELETE')
            result = requests.delete(url, json=payload, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result
