import os
import json

import requests


class BillingTimeEntryWebInterface:
    url = os.getenv("URL")
    headers = {"authtoken": os.getenv("TOKEN"),
               "accept": "application/vnd.manageengine.sdp.v3+json"}

    @classmethod
    def add_a_time_entry(cls, request_id, worklog):
        url = cls.url + f"/requests/{request_id}/worklogs"
        params = {"input_data": json.dumps(worklog)}
        response = requests.post(url, headers=cls.headers, params=params, verify=False)
        return response.json()
