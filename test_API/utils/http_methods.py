import requests


"""Список HTTP методов"""


class HttpMethods:
    headers = {'accept': 'application/json'}
    headers_out = {'accept': '*/*'}
    cookie = ''

    @staticmethod
    def get(url):
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def post(url, payload):
        result = requests.post(url, json=payload, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def put(url, payload):
        result = requests.put(url, json=payload, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def delete(url, payload):
        result = requests.get(url, json=payload, headers=HttpMethods.headers_out, cookies=HttpMethods.cookie)
        return result
