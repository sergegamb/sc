import os
import json

import requests


class RequestWebInterface:
    url = os.getenv("URL") + "/requests"
    headers = {"authtoken": os.getenv("TOKEN"),
               "accept": "application/vnd.manageengine.sdp.v3+json"}

    @staticmethod
    def create_new_request(request_data: dict):
        request = request_data
        return request

    @classmethod
    def view_request(cls, request_id):
        url = cls.url + "/" + request_id
        response = requests.get(url, headers=cls.headers, verify=False)
        return response.json()

    @classmethod
    def view_all_requests(cls, list_info):
        params = {"input_data": json.dumps(list_info)}
        response = requests.get(cls.url, headers=cls.headers, params=params, verify=False)
        return response.json()

    @classmethod
    def update_request(cls, request_id, request):
        url = f"{cls.url}/{request_id}"
        params = {"input_data": json.dumps(request)}
        response = requests.put(url, headers=cls.headers, params=params, verify=False)
        return response.json()