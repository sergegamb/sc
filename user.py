# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    user.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: serge <sgamb2000@gmail.com>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/06 03:08:14 by serge             #+#    #+#              #
#    Updated: 2024/05/06 03:13:55 by serge            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class UserWebInterface:
    @staticmethod
    def get_user_by_id(user_id: int):
        user = {
                "name": f"user{user_id}",
                "email_id": f"user{user_id}@sound.me",
        }
        return user

    @staticmethod
    def get_user_by_email_id(email_id: str):
        name = email_id.split("@")[0]
        user = {
                "name": name,
                "email_id": email_id,
        }
        return user
