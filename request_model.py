from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Resolution(BaseModel):
    resolution_attachments: List
    content: Any


class AssignedTime(BaseModel):
    display_value: str
    value: str


class ProfilePic(BaseModel):
    content_url: str = Field(..., alias='content-url')


class Account(BaseModel):
    name: str
    id: str


class Requester(BaseModel):
    email_id: str | None
    phone: Any
    name: str
    mobile: Any
    profile_pic: ProfilePic
    org_user_status: str
    id: str
    account: Optional[Account] = None


class Status(BaseModel):
    color: str | None
    name: str
    id: int


class ServiceCategory(BaseModel):
    id: str


class Template(BaseModel):
    is_service_template: bool
    service_category: ServiceCategory
    name: str
    id: str


class AttachedBy(BaseModel):
    email_id: Any
    phone: Any
    name: str
    mobile: Any
    profile_pic: Any
    is_vipuser: bool
    org_user_status: str
    id: str


class Size(BaseModel):
    display_value: str
    value: int


class AttachedOn(BaseModel):
    display_value: str
    value: str


class Attachment(BaseModel):
    module: str
    description: Any
    attached_by: AttachedBy
    content_type: str
    size: Size
    name: str
    attached_on: AttachedOn
    content_url: str
    id: str


class RespondedTime(BaseModel):
    display_value: str
    value: str


class ResponseTimeElapsed(BaseModel):
    display_value: str
    value: str


class Mode(BaseModel):
    name: str
    id: str


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
    email_id: Any
    phone: Any
    name: str
    mobile: Any
    profile_pic: ProfilePic1
    is_vipuser: bool
    org_user_status: str
    id: str


class ScheduledEndTime(BaseModel):
    display_value: str
    value: str


class LastUpdatedTime(BaseModel):
    display_value: str
    value: str


class ScheduledStartTime(BaseModel):
    display_value: str
    value: str


class ProfilePic2(BaseModel):
    content_url: str = Field(..., alias='content-url')


class Account1(BaseModel):
    name: str
    id: str


class Technician(BaseModel):
    email_id: str
    phone: str | None
    name: str
    mobile: str | None
    profile_pic: ProfilePic2
    is_vipuser: bool
    org_user_status: str
    id: str
    account: Optional[Account1] = None


class Category(BaseModel):
    name: str
    id: str


class Account2(BaseModel):
    country: Any
    inactive: bool
    timezone: Any
    name: str
    industry: Any
    id: str
    ciid: str


class Priority(BaseModel):
    color: str
    name: str
    id: str


class Request(BaseModel):
    ola_due_by_time: Any
    resolution: Resolution
    onhold_time: Any
    is_trashed: bool
    fr_sla_violated_group: Any
    id: str
    assigned_time: AssignedTime | None
    requester: Requester
    cancel_requested_by: Any
    sla_violated_technician: Any
    item: Any
    has_resolution_attachments: bool
    sla: Any
    priority: Priority | None
    sla_violated_group: Any
    tags: List
    has_notes: bool
    is_current_ola_violated: Any
    image_token: str
    udf_fields: Dict[str, Any]
    status: Status
    template: Template
    attachments: List[Attachment]
    request_type: Any
    cancel_requested_time: Any
    is_unknown: bool
    responded_time: Optional[RespondedTime] = None
    chat_type: int
    is_service_request: bool
    billing_status: Any
    cancel_requested: bool
    product: Any
    has_attachments: bool
    has_linked_requests: bool
    is_billable: bool
    response_time_elapsed: Optional[ResponseTimeElapsed] = None
    subject: str
    linked_to_request: Any
    mode: Optional[Mode] = None
    is_read: bool
    lifecycle: Lifecycle
    reason_for_cancel: Any
    group: Group
    email_to: List[str]
    created_time: CreatedTime
    approval_status: Any
    subaccount: Any
    service_category: ServiceCategory1
    created_by: CreatedBy
    scheduled_end_time: ScheduledEndTime | None
    first_response_due_by_time: Any
    last_updated_time: LastUpdatedTime | None
    subcategory: Any
    email_cc: List
    onhold_scheduler: Optional[Any] = None
    scheduled_start_time: ScheduledStartTime | None
    email_ids_to_notify: Optional[List] = None
    is_request_contract_applicable: bool
    notification_status: str | None
    description: str | None
    has_dependency: bool
    has_conversation: bool
    fr_sla_violated_technician: Any
    callback_url: Any
    is_shared: bool
    accountcontract: Any
    request_template_task_ids: List
    is_reopened: bool
    has_draft: bool
    is_overdue: bool
    technician: Technician | None
    due_by_time: Any
    is_first_response_overdue: bool
    cancel_requested_is_pending: bool
    recommend_template: Any
    unreplied_count: Any
    category: Category | None
    maintenance: Any
    account: Account2 | None


class ResponseStatus(BaseModel):
    status_code: int
    status: str


class ViewRequestResponse(BaseModel):
    request: Optional[Request] = None
    response_status: Optional[ResponseStatus] = None
