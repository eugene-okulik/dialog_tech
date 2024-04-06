import allure
import requests

from test_api_objects.endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):
    expected_response = 'Object with id = {} has been deleted.'

    @allure.step('Delete object by id')
    def delete_object(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/{object_id}',
            headers=headers
        )
        self.json = self.response.json()

    @allure.step('Check response message')
    def check_response_message(self, object_id):
        assert self.json['message'] == self.expected_response.format(object_id)
