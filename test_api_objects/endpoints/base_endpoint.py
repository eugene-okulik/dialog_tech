import allure


class BaseEndpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Check that title is the same as sent')
    def check_response_title_is_correct(self, title):
        assert self.json['title'] == title

    @allure.step('Check response status code')
    def check_status_code(self, code):
        assert self.response.status_code == code, f'status code {self.response.status_code} is not {code}'

    @allure.step('Check response object name')
    def check_object_name(self, name):
        assert self.json['name'] == name, 'Object name does not match'

    @allure.step('Check response object data')
    def check_object_data(self, data):
        assert self.json['data'] == data, 'Object data does not match'

    @allure.step('Check response object id')
    def check_response_object_id(self, object_id):
        assert self.json['id'] == object_id, 'IDs do not match'
