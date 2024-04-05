import allure
import requests

from test_api_objects.endpoints.base_endpoint import BaseEndpoint


class FullUpdateObject(BaseEndpoint):

    @allure.step('Full update a object')
    def make_changes_in_object(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{object_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
