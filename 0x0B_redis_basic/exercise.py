#!/usr/bin/env python3
"""
Cache class
"""
from typing import Union
import redis
import uuid


class Cache():
    """ cache class """

    def __init__(self) -> None:
        """ init """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ generate a random key """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
