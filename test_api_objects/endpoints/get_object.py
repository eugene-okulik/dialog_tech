import allure
import requests

from test_api_objects.endpoints.base_endpoint import BaseEndpoint


class GetObject(BaseEndpoint):

    @allure.step('Get object by id')
    def get_object(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}/{object_id}',
            headers=headers
        )
        self.json = self.response.json()
