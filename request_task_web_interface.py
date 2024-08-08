import os

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
