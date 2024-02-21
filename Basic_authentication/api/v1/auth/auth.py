#!/usr/bin/env python3
""" Manager API Authentication """
from flask import request
from typing import List, TypeVar


class Auth():
    """ class manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check if authentication is required for a given path. """
        return False

    def authorization_header(self, request=None) -> str:
        """ Get the authorization header from the Flask request object. """
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user from the Flask request object. """
        return request
