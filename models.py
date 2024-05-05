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

from pydantic import BaseModel, Field
from typing import Any


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


class Resolution(BaseModel):
    resolution_attachments: list
    content: Any


class OnholdTime(BaseModel):
    display_value: str
    value: str


class AssignedTime(BaseModel):
    display_value: str
    value: str


class ProfilePic(BaseModel):
    content_url: str = Field(..., alias='content-url')


class Account(BaseModel):
    name: str
    id: str


class Requester(BaseModel):
    email_id: str
    phone: Any
    name: str
    mobile: Any
    profile_pic: ProfilePic
    is_vipuser: bool
    org_user_status: str
    id: str
    account: Account


class Priority(BaseModel):
    color: str
    name: str
    id: str


class Status(BaseModel):
    color: str
    name: str
    id: str


class ServiceCategory(BaseModel):
    id: str


class Template(BaseModel):
    is_service_template: bool
    service_category: ServiceCategory
    name: str
    id: str


class RespondedTime(BaseModel):
    display_value: str
    value: str


class ProductType(BaseModel):
    id: str


class Product(BaseModel):
    part_no: str
    product_type: ProductType
    inactive: bool
    warranty_period_years: str
    name: str
    comment: str
    id: str
    warranty_period_months: str


class ResponseTimeElapsed(BaseModel):
    display_value: str
    value: str


class Lifecycle(BaseModel):
    name: str
    id: str


class Group(BaseModel):
    name: str
    id: str


class CreatedTime(BaseModel):
    display_value: str
    value: str


class ServiceCategory1(BaseModel):
    name: str
    id: str
    ciid: str


class ProfilePic1(BaseModel):
    content_url: str = Field(..., alias='content-url')


class CreatedBy(BaseModel):
    email_id: str
    phone: str
    name: str
    mobile: str
    profile_pic: ProfilePic1
    is_vipuser: bool
    org_user_status: str
    id: str


class LastUpdatedTime(BaseModel):
    display_value: str
    value: str


class ProfilePic2(BaseModel):
    content_url: str = Field(..., alias='content-url')


class Technician(BaseModel):
    email_id: str
    phone: str
    name: str
    mobile: Any
    profile_pic: ProfilePic2
    is_vipuser: bool
    org_user_status: str
    id: str


class Country(BaseModel):
    id: str


class Timezone(BaseModel):
    id: str


class Account1(BaseModel):
    country: Country
    inactive: bool
    timezone: Timezone
    name: str
    industry: Any
    id: str
    ciid: str


class Request(BaseModel):
    subject: str


class ResponseStatus(BaseModel):
    status_code: int
    status: str


class Model(BaseModel):
    request: Request
    response_status: ResponseStatus
