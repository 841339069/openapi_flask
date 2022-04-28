# -*- coding: utf-8 -*-
# @Author  : gxw
# @Time    : 2022/4/29 10:50
from typing import Optional, List, Dict

from pydantic import BaseModel

from .common import ExternalDocumentation
from .component import Components
from .info import Info
from .path import PathItem
from .server import Server
from .tag import Tag

OPENAPI3_REF_PREFIX = '#/components/schemas'
OPENAPI3_REF_TEMPLATE = OPENAPI3_REF_PREFIX + '/{model}'


class APISpec(BaseModel):
    openapi: str
    info: Info
    servers: Optional[List[Server]] = None
    paths: Dict[str, PathItem] = None
    components: Optional[Components] = None
    security: Optional[List[Dict[str, List[str]]]] = None
    tags: Optional[List[Tag]] = None
    externalDocs: Optional[ExternalDocumentation] = None
