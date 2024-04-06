import allure
import requests

from test_api_objects.endpoints.base_endpoint import BaseEndpoint


class GetObjectsByIDs(BaseEndpoint):

    @allure.step('Get object by id')
    def get_objects(self, object_ids, headers=None):
        params = {'id': object_ids}
        headers = headers if headers else self.headers
        self.response = requests.get(
            self.url,
            headers=headers,
            params=params
        )
        self.json = self.response.json()

    @allure.step('Check response object ids')
    def check_objects_ids(self, object_ids):
        response_ids = [obj['id'] for obj in self.json]
        assert all(obj_id in response_ids for obj_id in object_ids), 'Not all requested objects returned'
