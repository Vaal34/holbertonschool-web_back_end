#!/usr/bin/env python3
"""
AUTH file
"""
import bcrypt
from db import DB
from user import User
import sqlalchemy
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """ hash password for security """
    return bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ generate uuid """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """ check is valid login """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode("utf-8"),
                              user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def create_session(self, email) -> str:
        """ create session """
        try:
            user = self._db.find_user_by(email=email)
            user.session_id = _generate_uuid()
            self._db._session.commit()
            return user.session_id
        except NoResultFound:
            return None
