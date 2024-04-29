# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loggers.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: serge <sgamb2000@gmail.com>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/29 14:58:49 by serge             #+#    #+#              #
#    Updated: 2024/04/29 15:04:45 by serge            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import logging


uvicorn_logger = logging.getLogger("uvicorn")
default_logger = uvicorn_logger
user_logger = default_logger
