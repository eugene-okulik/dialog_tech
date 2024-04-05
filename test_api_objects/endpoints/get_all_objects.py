import allure
import requests

from test_api_objects.endpoints.base_endpoint import BaseEndpoint


class GetAllObjects(BaseEndpoint):

    @allure.step('Get all objects')
    def get_objects(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            self.url,
            headers=headers
        )
        self.json = self.response.json()

    @allure.step('Check objects count')
    def check_objects_count(self, count):
        assert len(self.json) == count, 'Not all objects returned'
