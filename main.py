# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: serge <sgamb2000@gmail.com>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/29 19:17:24 by serge             #+#    #+#              #
#    Updated: 2024/05/06 03:17:52 by serge            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from interfaces import UserInterface, RequestInterface, TaskInterface
from models import User


email_id = "sgamb2000@gmail.com"
user_id = 3


def test_get_by_email():
    user = UserInterface.get_by_email(email_id)
    assert type(user) is User
    assert user.name == "sgamb2000"


def test_get_by_id():
    user2 = UserInterface.get_by_id(user_id)
    assert user2.name == "user3"
    assert "sound.me" in user2.email_id


def test_post_request():
    request_data = {
        "subject": "post_Request"
    }
    request = RequestInterface.add(request_data)
    assert request.subject == "post_Request"


def test_list_task():
    tasks = TaskInterface.list()
    assert len(tasks) == 12
    assert tasks.pop().id == "38"


def main():
    test_get_by_email()
    test_get_by_id()
    test_post_request()
    test_list_task()


if __name__ == "__main__":
    main()
