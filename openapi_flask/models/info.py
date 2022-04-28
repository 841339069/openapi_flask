# -*- coding: utf-8 -*-
# @Author  : gxw
# @Time    : 2022/4/29 10:50
from typing import Optional

from pydantic import BaseModel, AnyUrl


class Contact(BaseModel):
    name: Optional[str] = None
    url: Optional[AnyUrl] = None


class License(BaseModel):
    name: str
    identifier: Optional[str] = None
    url: Optional[AnyUrl] = None


class Info(BaseModel):
    title: str
    version: str
    summary: Optional[str] = None
    description: Optional[str] = None
    termsOfService: Optional[AnyUrl] = None
    contact: Optional[Contact] = None
    license: Optional[License] = None
