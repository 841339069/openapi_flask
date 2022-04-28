# -*- coding: utf-8 -*-
# @Author  : gxw
# @Time    : 2022/4/29 10:50
from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, Field

from .common import Schema, Reference


class ParameterInType(str, Enum):
    query = "query"
    header = "header"
    path = "path"
    cookie = "cookie"


class Parameter(BaseModel):
    name: str
    in_: ParameterInType = Field(..., alias="in")  # ... is REQUIRED
    description: Optional[str] = None
    required: Optional[bool] = None
    schema_: Optional[Union[Schema, Reference]] = Field(None, alias="schema")
