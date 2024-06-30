# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    interfaces.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: serge <sgamb2000@gmail.com>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/29 13:05:33 by serge             #+#    #+#              #
#    Updated: 2024/06/30 07:52:35 by serge            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from .user import UserWebInterface
from .request import RequestWebInterface
from .task import TaskWebInterface
from .models import User, Request
from .task_model import Model as TaskListResponse


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
    def list(cls, input_data: dict = None):
        input_data = """
        {
    "list_info": {
        "row_count": "12",
        "start_index": "2",
        "sort_fields": [
            {
                "field": "title",
                "order": "asc"
            },
            {
                "field": "created_time",
                "order": "desc"
            }
        ],
        "filter_by": {
            "id": "7"
        },
        "search_criteria": {
            "field": "account.name",
            "condition": "is not",
            "values": [
                "TESTACCOUNT1"
            ],
            "children": [
                {
                    "field": "additional_cost",
                    "condition": "lte",
                    "values": [
                        100
                    ],
                    "logical_operator": "AND"
                },
                {
                    "field": "marked_owner.name",
                    "condition": "like",
                    "values": [
                        "Howard Stern"
                    ],
                    "logical_operator": "OR"
                }
            ]
        },
        "fields_required": [
            "title",
            "id",
            "status",
            "additional_cost",
            "created_time",
            "account"
        ]
    }
}"""
        task_list_response = TaskListResponse(**TaskWebInterface.list(input_data))
        return task_list_response.tasks
