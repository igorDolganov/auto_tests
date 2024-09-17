from utils.http_methods import *

base_URL = 'https://rahulshettyacademy.com'
key = '?key =qaclick123'

"""классы методов любого проекта"""


class GoogleMapsAPI:

    """метод для создания новой локации"""
    @staticmethod
    def create_new_place():

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
            }

        post_resource = '/maps/api/place/add/json'  # ресурс метода POST
        post_url = base_URL+post_resource+key
        result_post = HttpMethods.post(post_url, json_for_create_new_place)
        return result_post

    """метод получения новой локации"""

    @staticmethod
    def get_new_place(place_id):

        get_resource = '/maps/api/place/get/json'
        get_url = base_URL+get_resource+key+'&place_id='+place_id
        result_get = HttpMethods.get(get_url)
        return result_get

    """метод для обновления новой локации"""

    @staticmethod
    def update_new_place(place_id):

        put_resource = '/maps/api/place/update/json'
        json_for_update_new_place = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        put_url = base_URL+put_resource+key
        result_put = HttpMethods.put(put_url, json_for_update_new_place)
        return result_put

    """метод удаления новой локации"""

    @staticmethod
    def delete_new_place(place_id):

        json_for_delete_new_place = {
            "place_id": place_id
        }
        delete_resource = '/maps/api/place/delete/json'
        delete_url = base_URL+delete_resource+key
        result_delete = HttpMethods.delete(delete_url, json_for_delete_new_place)
        return result_delete
