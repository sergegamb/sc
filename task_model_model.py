from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class CreatedTime(BaseModel):
    display_value: str
    value: str


class ProfilePic(BaseModel):
    content_url: str = Field(..., alias='content-url')


class Account(BaseModel):
    name: str
    id: str


class CreatedBy(BaseModel):
    email_id: str
    phone: str
    name: str
    mobile: Any
    profile_pic: ProfilePic
    is_vipuser: bool
    org_user_status: str
    id: str
    account: Account


class EstimatedEffort(BaseModel):
    display_value: str
    hours: str
    minutes: str
    days: str


class Status(BaseModel):
    color: str
    name: str
    id: str


class Task(BaseModel):
    template: Any
    percentage_completion: int
    attachments: List
    email_before: str
    description: Any
    title: str
    type: Any
    overdue: bool
    additional_cost: str
    actual_end_time: Any
    id: str
    actual_start_time: Any
    owner: Any
    created_time: CreatedTime
    associated_entity: str
    priority: Any
    created_by: CreatedBy
    due_by_time: Any
    scheduled_end_time: Any
    marked_owner: Any
    site: Any
    estimated_effort: EstimatedEffort
    issitevisit: bool
    account: Any
    scheduled_start_time: Any
    status: Status


class ResponseStatus(BaseModel):
    status_code: int
    status: str


class Model(BaseModel):
    task: Task
    response_status: ResponseStatus
