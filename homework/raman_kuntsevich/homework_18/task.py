import requests


def new_object():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        headers=headers,
        json=body)
    return response.json()['id']


def clear(obj_id):
    requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')


def get_all_objects():
    response = requests.get('https://api.restful-api.dev/objects')
    assert response.status_code == 200, 'Status code is incorrect'
    assert len(response.json()) == 13, 'Not all objects returned'


def get_objects_by_ids():
    params = {'id': ['1', '3', '5', '13']}
    response = requests.get(
        'https://api.restful-api.dev/objects',
        params=params
    )
    response_ids = [obj['id'] for obj in response.json()]
    assert response.status_code == 200, 'Status code is incorrect'
    assert all(obj_id in response_ids for obj_id in params['id']), 'Not all requested objects returned'


def get_object():
    obj_id = '13'
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['id'] == obj_id, 'IDs do not match'


def add_object():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        headers=headers,
        json=body)
    response_body = response.json()
    assert response.status_code == 200, 'Status code is incorrect'
    assert 'id' in response_body, 'Object has no id'
    assert response_body['name'] == body['name'], 'Object name does not match'
    assert response_body['data'] == body['data'], 'Object data does not match'
    clear(response_body['id'])


def update_object():
    obj_id = new_object()
    body = {
        "name": "Apple MacBook Pro 16 UPD",
        "data": {
            "year": 2020,
            "price": 2000,
            "CPU model": "Intel Core i9 UPD",
            "Hard disk size": "1 TB UPD"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'https://api.restful-api.dev/objects/{obj_id}',
        headers=headers,
        json=body)
    response_body = response.json()
    assert response_body['id'] == obj_id, 'IDs do not match'
    assert response_body['name'] == body['name'], 'Object name does not match'
    assert response_body['data'] == body['data'], 'Object data does not match'
    clear(obj_id)


def partially_update_object():
    obj_id = new_object()
    body = {
        "name": "Apple MacBook Pro 16 PATCHED",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{obj_id}',
        headers=headers,
        json=body)
    response_body = response.json()
    assert response_body['id'] == obj_id, 'IDs do not match'
    assert response_body['name'] == body['name'], 'Object name does not match'
    clear(obj_id)


def delete_object():
    obj_id = new_object()
    expected_response = 'Object with id = {} has been deleted.'
    response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    response_body = response.json()
    assert response_body['message'] == expected_response.format(obj_id)


get_all_objects()
get_objects_by_ids()
get_object()
add_object()
update_object()
partially_update_object()
delete_object()
