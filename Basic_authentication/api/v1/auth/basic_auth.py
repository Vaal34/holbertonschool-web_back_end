#!/usr/bin/env python3
""" Manager API Authentication """
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ class BasicAuth inerith from Auth """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ returns the Base64 part of the Authorization header """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header.startswith("Basic ") is False:
            return None
        else:
            return authorization_header[6:]
