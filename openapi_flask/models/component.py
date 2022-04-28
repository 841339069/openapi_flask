# -*- coding: utf-8 -*-
# @Author  : gxw
# @Time    : 2022/4/29 10:50
from typing import Optional, Dict, Union

from pydantic import BaseModel

from .common import Schema, Reference
from .security import SecurityScheme


class Components(BaseModel):
    schemas: Optional[Dict[str, Union[Schema, Reference]]] = None
    securitySchemes: Optional[Dict[str, Union[SecurityScheme, Reference]]] = None
