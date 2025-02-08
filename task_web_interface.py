import json
import os

import requests


class TaskWebInterface:
    url = os.getenv("URL") + "/tasks"
    headers = {"authtoken": os.getenv("TOKEN"),
               "accept": "application/vnd.manageengine.sdp.v3+json"}

    @classmethod
    def list(cls, input_data: dict):  # Todo: play with types
        params = {"input_data": json.dumps(input_data)}
        response = requests.get(cls.url, headers=cls.headers, params=params, verify=False)
        return response.json()

    @classmethod
    def add(cls, input_data: dict):
        params = {"input_data": json.dumps(input_data)}
        response = requests.post(cls.url, headers=cls.headers, params=params, verify=False)
        return response.json()

    @classmethod
    def get(cls, task_id: str):
        url = cls.url + "/" + task_id
        response = requests.get(url, headers=cls.headers, verify=False)
        return response.json()

    @classmethod
    def delete(cls, task_id):
        url = cls.url + "/" + task_id
        response = requests.delete(url, headers=cls.headers, verify=False)
        return response.json()

    @classmethod
    def update(cls, task_id, task):
        url = cls.url + f"/{task_id}"
        params = {"input_data": json.dumps(task)}
        response = requests.put(url, headers=cls.headers, params=params, verify=False)
        return response.json()