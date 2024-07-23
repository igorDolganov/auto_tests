from requests import Response
from utils.check import *
from utils.api import *

"""создание, удаление и изменение локации"""


class TestCreatePlace:
    def test_create_new_place(self):

        print("Метод POST")
        result_post: Response = GoogleMapsAPI.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Check.check_status_code(result_post, 200)

        print('Метод GET POST')
        result_get: Response = GoogleMapsAPI.get_new_place(place_id)
        Check.check_status_code(result_get, 200)

        print('Метод PUT')
        result_put: Response = GoogleMapsAPI.update_new_place(place_id)
        Check.check_status_code(result_put, 200)

        print('Метод GET PUT')
        result_get: Response = GoogleMapsAPI.get_new_place(place_id)

        print('Метод DELETE')
        result_delete: Response = GoogleMapsAPI.delete_new_place(place_id)
        Check.check_status_code(result_delete, 200)

        print('Метод GET DELETE')
        result_get: Response = GoogleMapsAPI.get_new_place(place_id)
