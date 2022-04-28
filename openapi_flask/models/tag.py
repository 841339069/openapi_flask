# -*- coding: utf-8 -*-
# @Author  : gxw
# @Time    : 2022/4/29 10:50
from typing import Optional

from pydantic import BaseModel

from .common import ExternalDocumentation


class Tag(BaseModel):
    name: str
    description: Optional[str] = None
    externalDocs: Optional[ExternalDocumentation] = None
