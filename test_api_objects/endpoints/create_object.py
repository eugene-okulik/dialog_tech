import allure
import requests

from test_api_objects.endpoints.base_endpoint import BaseEndpoint


class CreateObject(BaseEndpoint):
    object_id = None

    @allure.step('Create new object')
    def create_new_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.object_id = self.json['id']

    @allure.step('Check response body has id')
    def check_object_has_id(self, response_body):
        assert 'id' in response_body, 'Object has no id'
