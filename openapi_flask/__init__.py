# -*- coding: utf-8 -*-
# @Author  : gxw
# @Time    : 2022/4/29 10:50

__version__ = '1.1.2'

import os

from .models.file import FileStorage
from .models.info import Info
from .models.oauth import OAuthConfig
from .models.security import HTTPBase, HTTPBearer, OAuth2, APIKey, OpenIdConnect
from .models.server import Server, ServerVariable
from .models.tag import Tag
from .models.validation_error import UnprocessableEntity
from .openapi import APIBlueprint
from .openapi import OpenAPI

if os.environ.get("WERKZEUG_RUN_MAIN") is None:
    print(f" * Powered by openapi-flask (version: {__version__})")
