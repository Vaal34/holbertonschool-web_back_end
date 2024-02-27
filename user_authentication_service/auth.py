#!/usr/bin/env python3
"""
AUTH file
"""
import bcrypt
from db import DB
from user import User
import sqlalchemy


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
        user = self._db._session.query(User).filter_by(email=email).first()
        if user:
            raise ValueError(f"User {email} already exists.")
        else:
            hashed_password = _hash_password(password)
            new_user = User(email=email, hashed_password=hashed_password)
            self._db._session.add(new_user)
            self._db._session.commit()
            return self._db
