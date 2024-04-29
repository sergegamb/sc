# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    models.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: serge <sgamb2000@gmail.com>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/29 12:12:29 by serge             #+#    #+#              #
#    Updated: 2024/04/29 18:56:57 by serge            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from pydantic import BaseModel


class User(BaseModel):
    name: str
    email_id: str


class SearchFields(BaseModel):
    email_id: str


class ListInfo(BaseModel):
    search_fields: SearchFields


class GetAll(BaseModel):
    list_info: ListInfo
    fields_required: list[str]
