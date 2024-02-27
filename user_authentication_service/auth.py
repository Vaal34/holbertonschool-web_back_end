#!/usr/bin/env python3
"""
AUTH file
"""
import bcrypt
from db import DB
from user import User
import sqlalchemy
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ hash password for security """
    return bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register user """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            hash_pwd = _hash_password(password)
            return self._db.add_user(email=email, hashed_password=hash_pwd)