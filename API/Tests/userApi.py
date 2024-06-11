from Utilites.methods import *

"""Авторизация"""


def users():
    url = 'https://apis.inbev.in-aim.dev/api/v1/auth'
    payload = {
        'login': 'User1',
        'passwd': 'User1'
    }
    res = requests.post(url,
                        headers={'accept': 'application/json',
                                 'Content-Type': 'application/json'},
                        json=payload)
    cookie = res.cookies
    print('AUTH Request ' + url + ' responded with ' + str(res.status_code))
    print(res.text)
    if res.status_code >= 400:
        print('ATTENTION - ERROR! AUTH Request ' + url + ' responded with ' + str(res.status_code))
        print(res.text)

    """Получение пользователя"""

    headers = {
        'accept': 'application/json'
    }
    res1 = requests.get('https://apis.inbev.in-aim.dev/api/v1/users/profile', cookies=cookie, headers=headers)
    print('GET User profile Request responded with ' + str(res1.status_code))
    print(res1.text)
    if res1.status_code >= 400:
        print('ATTENTION - ERROR! GET Request responded with ' + str(res1.status_code))
        print(res1.text)

    """Получить список Пользователей"""

    res2 = requests.get('https://apis.inbev.in-aim.dev/api/v1/users?select={"limit":10,"page":1,"tableIdentifier":"usersList","params":{}}',cookies=cookie, headers=headers)
    print("GET group of users responded with " + str(res2.status_code))
    if res2.status_code >= 400:
        print('ATTENTION - ERROR! GET group of users responded with  ' + str(res2.status_code))
        print(res2.text)

    """Создание нового юзера"""

    letters = string.printable
    random_name = ''.join(random.choice(letters) for i in range(5))
    payload_create = {
        "entity": {
            "dirid": True,
            "login": 'test'+random_name,
            "eMail": "newmail@mail.com",
            "phone": "+79191112234",
            "status": 2,
            "name": 'test'+random_name,
            "loginTypeUsId": 2,
            "useBreadcrumb": True,
            "expiredDate": "2023-02-01T00:00:00.000Z",
            "notes": "Autotest user created"
        },
        "links": []
    }
    res3 = requests.post('https://apis.inbev.in-aim.dev/api/v1/users', json=payload_create, cookies=cookie, headers=headers)
    print("User create with " + str(res3.status_code))
    print(res3.text)
    check = res3.json()
    check_info = str(check.get('userUsid'))
    print(check_info)

    """Обновление юзера"""

    payload_update = {
        "entity": {
            "dirid": True,
            "login": 'test' + random_name,
            "eMail": "newmail@mail.com",
            "phone": "+79191112234",
            "status": 2,
            "name": 'test' + random_name,
            "loginTypeUsId": 2,
            "useBreadcrumb": True,
            "expiredDate": "2023-02-01T00:00:00.000Z",
            "notes": "Autotest user updated"
        },
        "links": []
    }
    res4 = requests.put('https://apis.inbev.in-aim.dev/api/v1/users/'+check_info, json=payload_update, cookies=cookie, headers=headers)
    print("User update with " + str(res4.status_code))
    print(res4.text)
    if res4.status_code >= 400:
        print('ATTENTION - ERROR! UPDATE USER responded with ' + str(res4.status_code))
        print(res4.text)

    """Получение обновлённого юзера"""

    res5 = requests.get('https://apis.inbev.in-aim.dev/api/v1/users/'+check_info, cookies=cookie, headers=headers)
    if res5.text == res4.text:
        print("All good!")
    else:
        print('ATTENTION - ERROR! GET UPDATE USER responded with ' + str(res5.status_code))
        print(res5.text)

    """Деактивация юзера"""

    res6 = requests.delete('https://apis.inbev.in-aim.dev/api/v1/users/'+check_info, cookies=cookie, headers=headers)
    print("User delete with " + str(res6.status_code))
    print(res6.text)
    if res6.status_code >= 400:
        print('ATTENTION - ERROR! DELETE USER responded with ' + str(res6.status_code))
        print(res6.text)

    """Получение деактивированного юзера"""

    res7 = requests.get('https://apis.inbev.in-aim.dev/api/v1/users/'+check_info, cookies=cookie, headers=headers)
    status = "Неактивний"
    assert status == "Неактивний"
    if status in res7.text:
        print("All good!")
    else:
        print('ATTENTION - ERROR! GET UPDATE USER responded with ' + str(res7.status_code))
        print(res7.text)

    """Логаут"""
    headers_out = {'accept': '*/*'}
    res_logout = requests.post('https://apis.inbev.in-aim.dev/api/v1/auth/logout',headers=headers_out, cookies=cookie)
    print("User logout with " + str(res_logout.status_code))
    print(res_logout.text)
    if res_logout.status_code >= 400:
        print('ATTENTION - ERROR! LOGOUT USER responded with ' + str(res_logout.status_code))
        print(res_logout.text)


users()
