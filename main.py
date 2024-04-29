# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: serge <sgamb2000@gmail.com>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/29 19:17:24 by serge             #+#    #+#              #
#    Updated: 2024/04/29 19:17:25 by serge            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from interfaces import UserInterface as ui
from models import User


email_id = "sgamb2000@gmail.com"
user_id = 3


def test_get_by_email():
    user = ui.get_by_email(email_id)
    assert type(user) is User
    assert user.name == "sgamb2000"


def test_get_by_id():
    user2 = ui.get_by_id(user_id)
    assert user2.name == "user3"
    assert "sound@me" in user2.email_id


def main():
    test_get_by_email()
    test_get_by_id()
