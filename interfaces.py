# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    interfaces.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: serge <sgamb2000@gmail.com>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/29 13:05:33 by serge             #+#    #+#              #
#    Updated: 2024/05/06 03:21:12 by serge            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from user import UserWebInterface
from request import RequestWebInterface
from models import User, Request


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
