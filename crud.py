# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    crud.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: serge <sgamb2000@gmail.com>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/29 14:58:09 by serge             #+#    #+#              #
#    Updated: 2024/04/29 19:16:28 by serge            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def get_user_by_id(user_id: int):
    # genereate user
    # get user from list
    # read user from db
    # get user from the repository
    # read actual user from the sc api

    user = {
            "name": f"user{user_id}",
            "email_id": f"user{user_id}@sound.me",
    }
    return user


def get_user_by_email_id(email_id: str):
    name = email_id.split("@")[0]
    user = {
            "name": name,
            "email_id": email_id,
    }
    return user


def create_new_request(request_data: dict):
    request = request_data
    return request
