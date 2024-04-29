# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    user.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: serge <sgamb2000@gmail.com>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/29 14:03:38 by serge             #+#    #+#              #
#    Updated: 2024/04/29 15:04:16 by serge            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from fastapi import APIRouter
from models import User
from interfaces import UserInterface
from loggers import user_logger


router = APIRouter(
        prefix="/user"
)


@router.get("/")
def get_user(email: str) -> User:
    user_logger.info("Retry")
    user = UserInterface.get_by_email(email)
