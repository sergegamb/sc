import os

import requests


class TaskWebInterface:
    @staticmethod
    def list(input_data: str):  # Todo: play with types
        url = "https://support.agneko.com/api/v3/tasks"
        headers = {"authtoken": os.getenv("TOKEN"),
                   "accept": "application/vnd.manageengine.sdp.v3+json"}
        params = {'input_data': input_data}
        response = requests.get(url, headers=headers, params=params, verify=False)
        return response.json()
