import logging

from .billing_time_entry_web_interface import (
    BillingTimeEntryWebInterface,
    GeneralTaskTimeEntryWebInterface,
    RequestTaskTimeEntryWebInterface
)
from .user import UserWebInterface
from .request_web_interface import RequestWebInterface
from .task_web_interface import TaskWebInterface
from .request_task_web_interface import RequestTaskWebInterface
from .models import User
from .request_model import ViewRequestResponse, Request
from .request_list_model import RequestListResponse
from .task_model import TaskListResponse, TaskGetResponse
from .task_model_model import Model as TaskResponse


logger = logging.getLogger(__name__)


GROUPS = {
    "Сергей Гамбарян": ["Входящие", "HELPDESK", "Хостинг", "Разработка"],
    "Илья Маракушев": ["ManageEngine", "Входящие", "HELPDESK", "Хостинг", "Разработка"],
    "Павел Тетерин": ["Входящие", "HELPDESK"],
    "Василий Гусев": ["ManageEngine", "HELPDESK", "Хостинг, облачные решения", "Разработка", "AGNEKO SNMPc", "Входящие"],
    "Вадим Гусев": ["ManageEngine", "Хостинг, облачные решения", "Разработка", "AGNEKO SNMPc", "Входящие"],
    "Дмитрий Одинцов": ["HELPDESK", "Хостинг, облачные решения", "Разработка", "Входящие"],
    "Александр Михайлов": ["ManageEngine", "Входящие", "HELPDESK"]
}

class UserInterface:
    @classmethod
    def get_by_email(cls, email: str):
        return User(**UserWebInterface.get_user_by_email_id(email))

    @classmethod
    def get_by_id(cls, user_id: int):
        return User(**UserWebInterface.get_user_by_id(user_id))


class RequestInterface:
    row_count = 7
    @classmethod
    def add(cls, data: dict):
        return Request(**RequestWebInterface.create_new_request(data))

    @classmethod
    def get(cls, request_id):
        api_response = RequestWebInterface.view_request(request_id)
        view_request_response = ViewRequestResponse(**api_response)
        return view_request_response.request

    @classmethod
    def to_work(cls, request_id):
        status_name = {"name": "В работе"}
        status = {"status": status_name}
        request = {"request": status}
        RequestWebInterface.update_request(request_id, request)

    @classmethod
    def to_hold(cls, request_id):
        status_name = {"name": "Приостановлена"}
        status = {"status": status_name}
        request = {"request": status}
        RequestWebInterface.update_request(request_id, request)

    @classmethod
    def list_all(cls, page):
        list_info = {
            "row_count": cls.row_count,
            "start_index": 1 + page * cls.row_count,
        }
        list_info = {"list_info": list_info}
        return cls.list(list_info)

    @classmethod
    def list_technician(cls, page, technician):
        list_info = {
            "row_count": cls.row_count,
            "start_index": 1 + page * cls.row_count,
        }
        status_not_compleate = {
            "field": "status.name",
            "condition": "is not",
            "value": "Выполнена",
            "logical_operator": "AND"
        }
        status_not_canceled = {
            "field": "status.name",
            "condition": "is not",
            "value": "Отменена",
            "logical_operator": "AND"
        }
        status_not_closed = {
            "field": "status.name",
            "condition": "is not",
            "value": "Закрыта",
            "logical_operator": "AND"
        }
        status_exclude = [status_not_closed, status_not_canceled, status_not_compleate]
        search_criteria = {
            "field": "technician.name",
            "condition": "is",
            "value": technician,
            "children": status_exclude
        }
        search_criteria = {"search_criteria": search_criteria}
        list_info.update(search_criteria)
        list_info = {"list_info": list_info}
        return cls.list(list_info)

    @classmethod
    def list_technician_group(cls, page, technician):
        list_info = {
            "row_count": cls.row_count,
            "start_index": 1 + page * cls.row_count,
        }
        search_criteria = {
            "field": "group.name",
            "condition": "is",
            "values": GROUPS[technician]
        }
        search_criteria = {"search_criteria": search_criteria}
        list_info.update(search_criteria)
        list_info = {"list_info": list_info}
        return cls.list(list_info)

    @classmethod
    def list(cls, list_info):
        api_response = RequestWebInterface.view_all_requests(list_info)
        request_list_response = RequestListResponse(**api_response)
        return request_list_response.requests


class TaskInterface:
    row_count = 10
    list_info = {
        "row_count": row_count,
        "sort_order": "desc",
        "sort_field": "id",
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
    def list(cls, page):
        list_info = cls.list_info
        list_info["start_index"] = (page - 1) * cls.row_count + 1
        list_info = {"list_info": list_info}
        api_response = TaskWebInterface.list(list_info)
        task_list_response = TaskListResponse(**api_response)
        return task_list_response.tasks

    @classmethod
    def get(cls, task_id):
        get_task_response = TaskGetResponse(**TaskWebInterface.get(task_id))
        return get_task_response.task

    @classmethod
    def delete(cls, task_id):
        TaskWebInterface.delete(task_id)

    @classmethod
    def to_done(cls, task_id):
        status_name = {"name": "Выполнена"}
        status = {"status": status_name}
        task = {"task": status}
        api_response = TaskWebInterface.update(task_id, task)
        logger.info(api_response)


class RequestTaskInterface:
    list_info = {
        "list_info": {
            "row_count": 10,
            "sort_order": "desc",
            "sort_field": "id",
            "search_criteria": {
                "field": "status.id",
                "condition": "is",
                "values": [3, 2],
            }
        }
    }

    @classmethod
    def add(cls, request_id, title):
        task = {
            "task": {
                "title": title,
                "status": {
                    "id": "2",
                    "name": "Open"
                }
            }
        }
        api_response = RequestTaskWebInterface.add_a_task(request_id, task)
        task_response = TaskResponse(**api_response)
        return task_response.task

    @classmethod
    def get(cls, request_id, task_id):
        api_response = RequestTaskWebInterface.get(task_id, request_id)
        get_task_response = TaskGetResponse(**api_response)
        return get_task_response.task

    @classmethod
    def list(cls, request_id):
        api_response = RequestTaskWebInterface.view_all_tasks(request_id,
                                                              cls.list_info)
        task_list_response = TaskListResponse(**api_response)
        return task_list_response.tasks

    @classmethod
    def delete(cls, request_id, task_id):
        api_response = RequestTaskWebInterface.delete_a_task(
            request_id,
            task_id
        )

    @classmethod
    def to_done(cls, request_id, task_id):
        status_name = {"name": "Выполнена"}
        status = {"status": status_name}
        task = {"task": status}
        api_response = RequestTaskWebInterface.update(request_id, task_id, task)
        logger.info(api_response)


class BillingTimeEntryInterface:
    @classmethod
    def add(cls, request_id, owner, start_time, end_time, description):
        owner = {"owner": {"name": owner}}
        start_time = {"value": start_time}
        end_time = {"value": end_time}
        description = {"description": description}
        worklog = {}
        worklog.update(owner)
        worklog["start_time"] = start_time
        worklog["end_time"] = end_time
        worklog.update(description)
        worklog = {"worklog": worklog}
        api_response = BillingTimeEntryWebInterface.add_a_time_entry(request_id, worklog)
        return api_response.get("response_status")


class GeneralTaskTimeEntryInterface:
    #TODO: DRY
    @classmethod
    def add(cls, task_id, owner, start_time, end_time, description):
        owner = {"owner": {"name": owner}}
        start_time = {"value": start_time}
        end_time = {"value": end_time}
        description = {"description": description}
        worklog = {}
        worklog.update(owner)
        worklog["start_time"] = start_time
        worklog["end_time"] = end_time
        worklog.update(description)
        worklog = {"worklog": worklog}
        api_response = GeneralTaskTimeEntryWebInterface.add_a_worklog(task_id, worklog)
        return api_response.get("response_status")


class RequestTaskTimeEntryInterface:
    #TODO: DRY
    @classmethod
    def add(cls, request_id, task_id, owner, start_time, end_time, description):
        owner = {"owner": {"name": owner}}
        start_time = {"value": start_time}
        end_time = {"value": end_time}
        description = {"description": description}
        worklog = {}
        worklog.update(owner)
        worklog["start_time"] = start_time
        worklog["end_time"] = end_time
        worklog.update(description)
        worklog = {"worklog": worklog}
        api_response = RequestTaskTimeEntryWebInterface.add_a_worklog(request_id, task_id, worklog)
        return api_response.get("response_status")