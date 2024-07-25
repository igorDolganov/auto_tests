import allure
from utils.check import *
from utils.api import *

"""создание, удаление и изменение локации"""


@allure.epic
class TestCreatePlace:
    @allure.description('CRUD location')
    def test_create_new_place(self):

        print("Метод POST")
        result_post: Response = GoogleMapsAPI.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Check.check_status_code(result_post, 200)
        Check.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Check.check_json_value(result_post, 'status', 'OK')

        print('Метод GET POST')
        result_get: Response = GoogleMapsAPI.get_new_place(place_id)
        Check.check_status_code(result_get, 200)
        # Check.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print('Метод PUT')
        result_put: Response = GoogleMapsAPI.update_new_place(place_id)
        Check.check_status_code(result_put, 200)
        Check.check_json_token(result_put, ['msg'])

        print('Метод DELETE')
        result_delete: Response = GoogleMapsAPI.delete_new_place(place_id)
        Check.check_status_code(result_delete, 200)
        Check.check_json_token(result_delete, ['status'])


