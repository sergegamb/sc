from .user import UserWebInterface
from .request import RequestWebInterface
from .task_web_interface import TaskWebInterface
from .models import User, Request
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


class TaskInterface:
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
    def list(cls, input_data: dict = None):
        input_data = {
            "list_info": {
                "row_count": 10,
                "sort_order": "desc",
                "sort_field": "id",
            }
        }
        task_list_response = TaskListResponse(**TaskWebInterface.list(input_data))
        return task_list_response.tasks

    @classmethod
    def get(cls, task_id):
        get_task_response = TaskGetResponse(**TaskWebInterface.get(task_id))
        return get_task_response.task
