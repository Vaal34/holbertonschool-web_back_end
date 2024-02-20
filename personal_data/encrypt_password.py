#!/usr/bin/env python3
""" encrypt password"""
import bcrypt


def hash_password(password: str) -> str:
    """ hash password """
    return bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())
