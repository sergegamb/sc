# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    interfaces.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: serge <sgamb2000@gmail.com>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/29 13:05:33 by serge             #+#    #+#              #
#    Updated: 2024/04/29 19:04:30 by serge            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from crud import get_user_by_email_id, get_user_by_id
from models import User


class UserInterface:
    @classmethod
    def get_by_email(cls, email: str):
        return User(**get_user_by_email_id(email))

    @classmethod
    def get_by_id(cls, user_id: int):
        return User(**get_user_by_id(user_id))
