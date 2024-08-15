import os
import json

import requests


class RequestTaskWebInterface:
    url = os.getenv("URL") + "/requests"
    headers = {"authtoken": os.getenv("TOKEN"),
               "accept": "application/vnd.manageengine.sdp.v3+json"}

    @classmethod
    def get(cls, task_id, request_id):
        url = cls.url + f"/{request_id}/tasks/{task_id}"
        response = requests.get(url, headers=cls.headers, verify=False)
        return response.json()

    @classmethod
    def add_a_task(cls, request_id, task):
        url = cls.url + f"/{request_id}/tasks"
        params = {"input_data": json.dumps(task)}
        response = requests.post(url, headers=cls.headers, params=params, verify=False)
        return response.json()

    @classmethod
    def view_all_tasks(cls, request_id, list_info):
        url = cls.url + f"/{request_id}/tasks"
        params = {"input_data": json.dumps(list_info)}
        response = requests.get(url, headers=cls.headers, params=params, verify=False)
        return response.json()

    @classmethod
    def delete_a_task(cls, request_id, task_id):
        url = cls.url + f"/{request_id}/tasks/{task_id}"
        response = requests.delete(url, headers=cls.headers, verify=False)
        return response.json()
