#!/usr/bin/env python3
""" Manager API Session Authentication """
from flask import request
from typing import List, TypeVar, Tuple
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
import json


class SessionAuth(Auth):
    """ class SessionUAuth inerith from Auth """
    pass
