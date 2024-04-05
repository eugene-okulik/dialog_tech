import pytest
from test_api_objects.endpoints.create_object import CreateObject
from test_api_objects.endpoints.full_update_object import FullUpdateObject
from test_api_objects.endpoints.partial_update_object import PartialUpdateObject
from test_api_objects.endpoints.get_all_objects import GetAllObjects
from test_api_objects.endpoints.get_object import GetObject
from test_api_objects.endpoints.get_objects_by_ids import GetObjectsByIDs
from test_api_objects.endpoints.delete_object import DeleteObject


from test_api_objects.api_utils import generate_random_body as random_body


@pytest.fixture()
def add_object_endpoint():
    return CreateObject()


@pytest.fixture()
def full_update_object_endpoint():
    return FullUpdateObject()


@pytest.fixture()
def partial_update_object_endpoint():
    return PartialUpdateObject()


@pytest.fixture()
def get_all_objects():
    return GetAllObjects()


@pytest.fixture()
def get_object_by_id():
    return GetObject()


@pytest.fixture()
def get_objects_by_ids():
    return GetObjectsByIDs()


@pytest.fixture()
def delete_object_by_id():
    return DeleteObject()


@pytest.fixture()
def object_id(add_object_endpoint, delete_object_by_id):
    payload = random_body()
    add_object_endpoint.create_new_object(payload)
    yield add_object_endpoint.object_id
    delete_object_by_id.delete_object(add_object_endpoint.object_id)


@pytest.fixture()
def new_object_ids(add_object_endpoint, delete_object_by_id, request):
    num_objects = request.param
    object_ids = []

    for _ in range(num_objects):
        add_object_endpoint.create_new_object(random_body())
        object_ids.append(add_object_endpoint.json['id'])

    yield object_ids

    for obj_id in object_ids:
        delete_object_by_id.delete_object(obj_id)
