import requests
import pytest
from faker import Faker


@pytest.fixture(scope='session', autouse=True)
def print_before_and_after_session():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(autouse=True)
def print_before_and_after_tests():
    print('before test')
    yield
    print('after test')


def get_random_body():
    return {
        "name": Faker().name(),
        "data": {
            "year": Faker().year(),
            "price": Faker().random_number(),
            "CPU model": Faker().word(),
            "Hard disk size": f'{Faker().random_int(1, 5)} TB'
        }
    }


def get_all_post_ids():
    response = requests.get('https://api.restful-api.dev/objects')
    return list(map(lambda obj: obj['id'], response.json()))


@pytest.fixture()
def new_object_ids(request):
    headers = {'Content-Type': 'application/json'}
    num_objects = request.param
    object_ids = []

    for _ in range(num_objects):
        response = requests.post(
            'https://api.restful-api.dev/objects',
            headers=headers,
            json=get_random_body())
        obj_id = response.json()['id']
        object_ids.append(obj_id)

    yield object_ids

    for obj_id in object_ids:
        requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')


def test_get_all_objects():
    get_all_post_ids()
    response = requests.get('https://api.restful-api.dev/objects')
    assert response.status_code == 200, 'Status code is incorrect'
    assert len(response.json()) == 13, 'Not all objects returned'


@pytest.mark.parametrize('new_object_ids', [1, 3, 5], indirect=True)
def test_get_objects_by_ids(new_object_ids):
    params = {'id': new_object_ids}
    response = requests.get(
        'https://api.restful-api.dev/objects',
        params=params
    )
    response_ids = [obj['id'] for obj in response.json()]
    assert response.status_code == 200, 'Status code is incorrect'
    assert all(obj_id in response_ids for obj_id in params['id']), 'Not all requested objects returned'


@pytest.mark.parametrize('new_object_ids', [1], indirect=True)
def test_get_object(new_object_ids):
    obj_id = new_object_ids[0]
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['id'] == obj_id, 'IDs do not match'


@pytest.mark.critical
@pytest.mark.parametrize('body', [get_random_body() for _ in range(3)])
def test_add_object(body):
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


@pytest.mark.parametrize('new_object_ids', [1], indirect=True)
def test_update_object(new_object_ids):
    obj_id = new_object_ids[0]
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


@pytest.mark.parametrize('new_object_ids', [1], indirect=True)
@pytest.mark.medium
def test_partially_update_object(new_object_ids):
    obj_id = new_object_ids[0]
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


def test_delete_object(new_object_id):
    expected_response = 'Object with id = {} has been deleted.'
    response = requests.delete(f'https://api.restful-api.dev/objects/{new_object_id}')
    response_body = response.json()
    assert response_body['message'] == expected_response.format(new_object_id)
