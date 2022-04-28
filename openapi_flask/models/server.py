# -*- coding: utf-8 -*-
# @Author  : gxw
# @Time    : 2022/4/29 10:50
from typing import Optional, List, Dict

from pydantic import BaseModel


class ServerVariable(BaseModel):
    default: str
    enum: Optional[List[str]] = None
    description: Optional[str] = None


class Server(BaseModel):
    url: str
    description: Optional[str] = None
    variables: Optional[Dict[str, ServerVariable]] = None
