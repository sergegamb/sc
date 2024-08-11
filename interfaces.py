from .user import UserWebInterface
from .request_web_interface import RequestWebInterface
from .task_web_interface import TaskWebInterface
from .request_task_web_interface import RequestTaskWebInterface
from .models import User
from .request_model import ViewRequestResponse, Request
from .request_list_model import RequestListResponse
from .task_model import TaskListResponse, TaskGetResponse
from .task_model_model import Model as TaskResponse


class UserInterface:
    @classmethod
    def get_by_email(cls, email: str):
        return User(**UserWebInterface.get_user_by_email_id(email))

    @classmethod
    def get_by_id(cls, user_id: int):
        return User(**UserWebInterface.get_user_by_id(user_id))


class RequestInterface:
    @classmethod
    def add(cls, data: dict):
        return Request(**RequestWebInterface.create_new_request(data))

    @classmethod
    def get(cls, request_id):
        view_requst_response = ViewRequestResponse(**RequestWebInterface.view_requst(request_id))
        return view_requst_response.request

    @classmethod
    def list(cls, list_info = None):
        request_list_response = RequestListResponse(**RequestWebInterface.view_all_requests(list_info))
        return request_list_response.requests


class TaskInterface:
    list_info = {
        "list_info": {
            "row_count": 10,
            "sort_order": "desc",
            "sort_field": "id",
        }
    }

    @classmethod
    def add(cls, title: str):
        input_data = {
            "task": {
                "title": title,
                "status": {
                    "id": "2",
                    "name": "Open"
                }
            }
        }
        task_add_response = TaskResponse(**TaskWebInterface.add(input_data))
        return task_add_response.task

    @classmethod
    def add_request_task(cls, request_id, title):
        # TODO: reduce duplication
        task = {
            "task": {
                "title": title,
                "status": {
                    "id": "2",
                    "name": "Open"
                }
            }
        }
        task_add_response = TaskResponse(**RequestTaskWebInterface.add_a_task(request_id, task))
        return task_add_response.task

    @classmethod
    def list(cls):
        task_list_response = TaskListResponse(**TaskWebInterface.list(cls.list_info))
        return task_list_response.tasks

    @classmethod
    def list_request_tasks(cls, request_id):
        task_list_response = TaskListResponse(**RequestTaskWebInterface.view_all_tasks(request_id, cls.list_info))
        return task_list_response.tasks

    @classmethod
    def get(cls, task_id):
        get_task_response = TaskGetResponse(**TaskWebInterface.get(task_id))
        return get_task_response.task

    @classmethod
    def get_request_task(cls, task_id, request_id):
        get_task_response = TaskGetResponse(**RequestTaskWebInterface.get(task_id, request_id))
        return get_task_response.task

    @classmethod
    def delete(cls, task_id):
        TaskWebInterface.delete(task_id)
