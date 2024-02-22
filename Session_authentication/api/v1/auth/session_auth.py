#!/usr/bin/env python3
""" Manager API Session Authentication """
from flask import request
from typing import List, TypeVar, Tuple
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
import json
import uuid


class SessionAuth(Auth):
    """ class SessionAuth inerith from Auth """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a Session ID for a user_id """
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        session_id = uuid.uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id
    
    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ that returns a User ID based on a Session ID """
        if session_id is None:
            return None
        if type(session_id) is not str:
            return None
        
        return self.user_id_by_session_id[session_id]