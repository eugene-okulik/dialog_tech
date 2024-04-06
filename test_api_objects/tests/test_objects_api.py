import pytest
import allure
from test_api_objects.api_utils import generate_random_body as random_body


@allure.feature('CRUD')
@allure.story('Create object')
@allure.title('Создание объекта')
@pytest.mark.critical
@pytest.mark.parametrize('body', [random_body() for _ in range(3)])
def test_create_object(add_object_endpoint, body):
    add_object_endpoint.create_new_object(payload=body)
    add_object_endpoint.check_status_code(200)
    add_object_endpoint.check_object_has_id(add_object_endpoint.json)
    add_object_endpoint.check_object_name(body['name'])
    add_object_endpoint.check_object_data(body['data'])


@allure.feature('CRUD')
@allure.story('Update object')
@allure.title('Полное обновление объекта')
def test_update_object(full_update_object_endpoint, object_id):
    body = random_body()
    full_update_object_endpoint.make_changes_in_object(object_id, payload=body)
    full_update_object_endpoint.check_status_code(200)
    full_update_object_endpoint.check_response_object_id(object_id)
    full_update_object_endpoint.check_object_name(body['name'])
    full_update_object_endpoint.check_object_data(body['data'])


@allure.feature('CRUD')
@allure.story('Update object')
@allure.title('Частичное обновление объекта')
@pytest.mark.medium
def test_partially_update_object(partial_update_object_endpoint, object_id):
    body = {"name": "Apple MacBook Pro 16 PATCHED"}
    partial_update_object_endpoint.make_changes_in_object(object_id, payload=body)
    partial_update_object_endpoint.check_status_code(200)
    partial_update_object_endpoint.check_response_object_id(object_id)
    partial_update_object_endpoint.check_object_name(body['name'])


@allure.feature('CRUD')
@allure.story('Read object')
@allure.title('Получение всех объектов')
def test_get_all_objects(get_all_objects):
    get_all_objects.get_objects()
    get_all_objects.check_status_code(200)
    get_all_objects.check_objects_count(13)


@allure.feature('CRUD')
@allure.story('Read object')
@allure.title('Получение нескольких объектов по id')
@pytest.mark.parametrize('new_object_ids', [1, 3, 5], indirect=True)
def test_get_objects_by_ids(new_object_ids, get_objects_by_ids):
    get_objects_by_ids.get_objects(new_object_ids)
    get_objects_by_ids.check_status_code(200)
    get_objects_by_ids.check_objects_ids(new_object_ids)


@allure.feature('CRUD')
@allure.story('Read object')
@allure.title('Получение объекта по id')
def test_get_object_by_id(object_id, get_object_by_id):
    get_object_by_id.get_object(object_id)
    get_object_by_id.check_status_code(200)
    get_object_by_id.check_response_object_id(object_id)


@allure.feature('CRUD')
@allure.story('Delete object')
@allure.title('Удаление объекта')
def test_delete_object(object_id, delete_object_by_id):
    delete_object_by_id.delete_object(object_id)
    delete_object_by_id.check_status_code(200)
    delete_object_by_id.check_response_message(object_id)
