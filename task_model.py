from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class ResponseStatu(BaseModel):
    status_code: int
    status: str


class SortField(BaseModel):
    field: str
    order: str


class FilterBy(BaseModel):
    id: int


class Child(BaseModel):
    condition: str
    field: str
    logical_operator: str
    values: List[str]


class SearchCriteria(BaseModel):
    condition: str
    field: str
    children: List[Child]
    values: List[str]


class ListInfo(BaseModel):
    sort_fields: List[SortField]
    has_more_rows: bool
    start_index: int
    fields_required: List[str]
    filter_by: FilterBy
    page: int
    start_count: int
    search_criteria: SearchCriteria
    row_count: int


class CreatedTime(BaseModel):
    display_value: str
    value: str


class CountryItem(BaseModel):
    id: str


class TimezoneItem(BaseModel):
    id: str


class Account(BaseModel):
    country: Optional[CountryItem]
    inactive: bool
    timezone: Optional[TimezoneItem]
    name: str
    industry: Any
    id: str
    ciid: str


class Status(BaseModel):
    color: str
    name: str
    id: str


class Task(BaseModel):
    created_time: CreatedTime
    baseURL: str
    additional_cost: str
    id: str
    account: Account
    status: Status


class Model(BaseModel):
    response_status: List[ResponseStatu]
    list_info: ListInfo
    tasks: List[Task]
