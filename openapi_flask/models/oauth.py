# -*- coding: utf-8 -*-
# @Author  : gxw
# @Time    : 2022/4/29 10:50


from typing import Dict, Optional

from pydantic import BaseModel


class OAuthConfig(BaseModel):
    """
    More information go to: https://github.com/swagger-api/swagger-ui/blob/master/docs/usage/oauth2.md
    """
    clientId: Optional[str] = None
    clientSecret: Optional[str] = None
    realm: Optional[str] = None
    appName: Optional[str] = None
    scopeSeparator: Optional[str] = None
    scopes: Optional[str] = None
    additionalQueryStringParams: Optional[Dict[str, str]] = None
    useBasicAuthenticationWithAccessCodeGrant: Optional[bool] = False
    usePkceWithAuthorizationCodeGrant: Optional[bool] = False
