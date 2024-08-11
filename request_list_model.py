from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class ResponseStatu(BaseModel):
    status_code: int
    status: str


class SearchFields(BaseModel):
    priority_name: str = Field(..., alias='priority.name')
    subject: str


class FilterBy(BaseModel):
    name: str


class ListInfo(BaseModel):
    has_more_rows: Optional[bool] = None
    start_index: Optional[int] = None
    sort_field: Optional[str] = None
    search_fields: Optional[SearchFields] = None
    total_count: Optional[int] = None
    filter_by: Optional[FilterBy] = None
    sort_order: Optional[str] = None
    get_total_count: Optional[str] = None
    row_count: Optional[int] = None


class Requester(BaseModel):
    email_id: Any
    phone: str | None
    name: str
    mobile: str | None
    id: str


class Template(BaseModel):
    is_service_template: bool
    name: str
    id: str


class CreatedTime(BaseModel):
    display_value: str
    value: str


class Priority(BaseModel):
    color: str
    name: str
    id: str


class CreatedBy(BaseModel):
    email_id: Any
    phone: str | None
    name: str
    mobile: str | None
    id: str


class Status(BaseModel):
    color: str
    name: str
    id: str


class Request(BaseModel):
    requester: Optional[Requester] = None
    template: Optional[Template] = None
    short_description: Optional[str] = None
    created_time: Optional[CreatedTime] = None
    product: Optional[Any] = None
    subject: Optional[str] = None
    subaccount: Optional[Any] = None
    time_elapsed: Optional[Any] = None
    is_overdue: Optional[bool] = None
    technician: Optional[Any] = None
    priority: Optional[Priority] = None
    created_by: Optional[CreatedBy] = None
    due_by_time: Optional[Any] = None
    is_service_request: Optional[bool] = None
    accountcontract: Optional[Any] = None
    id: Optional[str] = None
    account: Optional[Any] = None
    status: Optional[Status] = None
    group: Optional[Any] = None


class RequestListResponse(BaseModel):
    response_status: List[ResponseStatu]
    list_info: ListInfo
    requests: List[Request]
