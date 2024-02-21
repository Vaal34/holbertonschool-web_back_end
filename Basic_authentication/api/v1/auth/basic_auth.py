#!/usr/bin/env python3
""" Manager API Authentication """
from flask import request
from typing import List, TypeVar, Tuple
from api.v1.auth.auth import Auth
from base64 import b64decode


class BasicAuth(Auth):
    """ class BasicAuth inerith from Auth """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ returns the Base64 part of the Authorization header """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header.startswith("Basic ") is False:
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Returns the decoded value of a Base64 string."""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            return b64decode(base64_authorization_header).decode('UTF-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """  returns the useremail and pswd from the Base64 decoded value. """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        else:
            split_str = decoded_base64_authorization_header.split(":")
            user_email = split_str[0]
            password = split_str[1]
            return user_email, password
