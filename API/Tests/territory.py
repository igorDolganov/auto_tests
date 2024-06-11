from Utilites.methods import *

"""Авторизация"""


def territory():
    url = 'https://apis.inbev.in-aim.dev/api/v1/auth'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    payload = {
        'login': 'User1',
        'passwd': 'User1'
    }
    res = requests.post(url,
                        headers=headers,
                        json=payload)
    cookie = res.cookies
    print('AUTH Request ' + url + ' responded with ' + str(res.status_code))
    print(res.text)
    if res.status_code >= 400:
        print('ATTENTION - ERROR! AUTH Request ' + url + ' responded with ' + str(res.status_code))
        print(res.text)

    res_ter = requests.get('https://apis.inbev.in-aim.dev/api/v1/territory/44F7E3D7-9515-4981-B158-051CA8345EAE', headers=headers, cookies=cookie)
    print('GET Territory Request responded with ' + str(res_ter.status_code))
    print(res_ter.text)
    if res_ter.status_code >= 400:
        print('ATTENTION - ERROR! GET Request responded with ' + str(res_ter.status_code))
        print(res_ter.text)

    res_ter1 = requests.get('https://apis.inbev.in-aim.dev/api/v1/territory?limit=10&page=1&sort[name]=ASC&sort[login]=DESC&user[contains]=22&params=%7B%22relationId%22%3A31%2C%22isAttached%22%3Afalse%7D&viewSettings=%7B%22columnList%22%3A%5B%22%D0%B8%D0%BC%D1%8F%20%D0%BA%D0%BE%D0%BB%D0%BE%D0%BD%D0%BA%D0%B8%201%22%2C%22%D0%B8%D0%BC%D1%8F%20%D0%BA%D0%BE%D0%BB%D0%BE%D0%BD%D0%BA%D0%B8%202%22%2C%22%D0%B8%D0%BC%D1%8F%20%D0%BA%D0%BE%D0%BB%D0%BE%D0%BD%D0%BA%D0%B8%203%22%5D%2C%22columnKeyList%22%3A%5B%22oid%22%2C%22name%22%2C%22email%22%5D%2C%22columnSize%22%3A%5B100%2C200%2C350%5D%2C%22oneLine%22%3Atrue%2C%22showFilter%22%3Afalse%7D&group=column1&group=column2&group=column3&column1Value1[column2Value1][column3Value3]=&saveFindParameters=false&tableIdentifier=geo&select=%7B%22limit%22%3A10%2C%22page%22%3A1%2C%22tableIdentifier%22%3A%22userViewObj%22%2C%22saveFindParameters%22%3Atrue%2C%22params%22%3A%7B%22relationId%22%3A%22277%22%2C%22isAttached%22%3Atrue%7D%7D',headers=headers, cookies=cookie)
    print('GET Group of Territory Request responded with ' + str(res_ter1.status_code))
    print(res_ter1.text)
    if res_ter1.status_code >= 400:
        print('ATTENTION - ERROR! GET Request responded with ' + str(res_ter1.status_code))
        print(res_ter1.text)

    letters = string.printable
    random_name = ''.join(random.choice(letters) for i in range(5))
    payload_create = {
        "entity": {
            "parentId": "AE3DE3C2-8E5C-489F-AD89-C718D925F901",
            "orgStructureCode": "SR47 Киров",
            "name": "тестовое имя"+random_name,
            "email": "tech.support@abinbevefes.com",
            "level": 6,
            "orgStructureOldId": 1000010339,
            "taxCode": "15300",
            "phoneNumber": "+79999999999",
            "status": 2
        },
        "links": []
    }
    res_ter2 = requests.post('https://apis.inbev.in-aim.dev/api/v1/territory', json=payload_create, headers=headers, cookies=cookie)
    print("Territory create with " + str(res_ter2.status_code))
    print(res_ter2.text)
    match = re.search(r'"orgStructureId":"([^"]+)"', res_ter2.text)
    org_id = match[1]
    print(org_id)





territory()