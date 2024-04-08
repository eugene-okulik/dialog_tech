from locust import HttpUser, task, between
from api_utils import generate_random_body as random_body
import random


class RestfulApiTest(HttpUser):
    wait_time = between(0.5, 3)
    new_objects_ids = []

    @task(1)
    def create_object(self):
        object_body = random_body()
        response = self.client.post('/objects', json=object_body)
        print(response)
        obj_id = response.json()['id']
        self.new_objects_ids.append(obj_id)

    @task(5)
    def read_object(self):
        if len(self.new_objects_ids) == 0:
            return
        self.client.get('/objects')
        obj_id = random.choice(self.new_objects_ids)
        self.client.get(f'/objects/{obj_id}', name='read object')

    @task(2)
    def update_object(self):
        if len(self.new_objects_ids) == 0:
            return
        updated_body = random_body()
        self.client.get('/objects')
        obj_id = random.choice(self.new_objects_ids)
        self.client.put(f'/objects/{obj_id}', json=updated_body, name='update object')
