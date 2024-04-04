import requests
import pytest
from faker import Faker
import allure


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


@allure.feature('CRUD')
@allure.story('Read object')
@allure.title('Получение всех объектов')
def test_get_all_objects():
    with allure.step('Send request'):
        response = requests.get('https://api.restful-api.dev/objects')
    with allure.step('Check status code'):
        assert response.status_code == 200, 'Status code is incorrect'
    with allure.step('Check objects count'):
        assert len(response.json()) == 13, 'Not all objects returned'


@allure.feature('CRUD')
@allure.story('Read object')
@allure.title('Получение нескольких объектов по id')
@pytest.mark.parametrize('new_object_ids', [1, 3, 5], indirect=True)
def test_get_objects_by_ids(new_object_ids):
    params = {'id': new_object_ids}
    with allure.step('Send request'):
        response = requests.get(
            'https://api.restful-api.dev/objects',
            params=params
        )
        response_ids = [obj['id'] for obj in response.json()]
    with allure.step('Check status code'):
        assert response.status_code == 200, 'Status code is incorrect'
    with allure.step('Check response object ids'):
        assert all(obj_id in response_ids for obj_id in params['id']), 'Not all requested objects returned'


@allure.feature('CRUD')
@allure.story('Read object')
@allure.title('Получение объекта по id')
@pytest.mark.parametrize('new_object_ids', [1], indirect=True)
def test_get_object(new_object_ids):
    obj_id = new_object_ids[0]
    with allure.step('Send request'):
        response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    with allure.step('Check status code'):
        assert response.status_code == 200, 'Status code is incorrect'
    with allure.step('Check response object id'):
        assert response.json()['id'] == obj_id, 'IDs do not match'


@allure.feature('CRUD')
@allure.story('Create object')
@allure.title('Создание объекта')
@pytest.mark.critical
@pytest.mark.parametrize('body', [get_random_body() for _ in range(3)])
def test_add_object(body):
    headers = {'Content-Type': 'application/json'}
    with allure.step('Send request'):
        response = requests.post(
            'https://api.restful-api.dev/objects',
            headers=headers,
            json=body)
        response_body = response.json()
    with allure.step('Check status code'):
        assert response.status_code == 200, 'Status code is incorrect'
    with allure.step('Check new object has id'):
        assert 'id' in response_body, 'Object has no id'
    with allure.step('Check new object has name'):
        assert response_body['name'] == body['name'], 'Object name does not match'
    with allure.step('Check new object has data'):
        assert response_body['data'] == body['data'], 'Object data does not match'


@allure.feature('CRUD')
@allure.story('Update object')
@allure.title('Полное обновление объекта')
@pytest.mark.parametrize('new_object_ids', [1], indirect=True)
def test_update_object(new_object_ids):
    with allure.step('Prepare test data'):
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
    with allure.step('Send request'):
        response = requests.put(
            f'https://api.restful-api.dev/objects/{obj_id}',
            headers=headers,
            json=body)
        response_body = response.json()
    with allure.step('Check updated object id'):
        assert response_body['id'] == obj_id, 'IDs do not match'
    with allure.step('Check updated object name'):
        assert response_body['name'] == body['name'], 'Object name does not match'
    with allure.step('Check updated object data'):
        assert response_body['data'] == body['data'], 'Object data does not match'


@allure.feature('CRUD')
@allure.story('Update object')
@allure.title('Частичное обновление объекта')
@pytest.mark.parametrize('new_object_ids', [1], indirect=True)
@pytest.mark.medium
def test_partially_update_object(new_object_ids):
    with allure.step('Prepare test data'):
        obj_id = new_object_ids[0]
        body = {
            "name": "Apple MacBook Pro 16 PATCHED",
        }
        headers = {'Content-Type': 'application/json'}
    with allure.step('Send request'):
        response = requests.patch(
            f'https://api.restful-api.dev/objects/{obj_id}',
            headers=headers,
            json=body)
        response_body = response.json()
    with allure.step('Check updated object id'):
        assert response_body['id'] == obj_id, 'IDs do not match'
    with allure.step('Check updated object name'):
        assert response_body['name'] == body['name'], 'Object name does not match'


@allure.feature('CRUD')
@allure.story('Delete object')
@allure.title('Удаление объекта')
@pytest.mark.parametrize('new_object_ids', [1], indirect=True)
def test_delete_object(new_object_ids):
    expected_response = 'Object with id = {} has been deleted.'
    obj_id = new_object_ids[0]
    with allure.step('Send request'):
        response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
        response_body = response.json()
    with allure.step('Check expected response'):
        assert response_body['message'] == expected_response.format(obj_id)
