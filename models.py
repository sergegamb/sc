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
    ola_due_by_time: Any
    resolution: Resolution
    onhold_time: OnholdTime
    is_trashed: bool
    fr_sla_violated_group: Any
    id: str
    assigned_time: AssignedTime
    requester: Requester
    cancel_requested_by: Any
    sla_violated_technician: Any
    item: Any
    has_resolution_attachments: bool
    sla: Any
    priority: Priority
    sla_violated_group: Any
    tags: list
    has_notes: bool
    is_current_ola_violated: Any
    image_token: str
    udf_fields: dict[str, Any]
    status: Status
    template: Template
    attachments: list
    request_type: Any
    cancel_requested_time: Any
    is_unknown: bool
    responded_time: RespondedTime
    chat_type: int
    is_service_request: bool
    billing_status: Any
    cancel_requested: bool
    product: Product
    has_attachments: bool
    has_linked_requests: bool
    is_billable: bool
    response_time_elapsed: ResponseTimeElapsed
    subject: str
    linked_to_request: Any
    is_read: bool
    lifecycle: Lifecycle
    reason_for_cancel: Any
    group: Group
    email_to: list
    created_time: CreatedTime
    approval_status: Any
    subaccount: Any
    service_category: ServiceCategory1
    created_by: CreatedBy
    scheduled_end_time: Any
    first_response_due_by_time: Any
    last_updated_time: LastUpdatedTime
    subcategory: Any
    email_cc: list
    scheduled_start_time: Any
    email_ids_to_notify: list
    is_request_contract_applicable: bool
    notification_status: Any
    description: str
    has_dependency: bool
    has_conversation: bool
    fr_sla_violated_technician: Any
    callback_url: Any
    is_shared: bool
    accountcontract: Any
    request_template_task_ids: list
    is_reopened: bool
    has_draft: bool
    is_overdue: bool
    technician: Technician
    due_by_time: Any
    is_first_response_overdue: bool
    cancel_requested_is_pending: bool
    recommend_template: Any
    unreplied_count: Any
    category: Any
    maintenance: Any
    account: Account1


class ResponseStatus(BaseModel):
    status_code: int
    status: str


class Model(BaseModel):
    request: Request
    response_status: ResponseStatus
