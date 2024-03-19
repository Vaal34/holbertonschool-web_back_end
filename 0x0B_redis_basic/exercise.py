#!/usr/bin/env python3
"""
Cache class
"""
from typing import Callable, Optional, Union
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

    def get(self, key: str, fn: Optional[Callable] = None):
        """  """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        # Get string data from Redis
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        # Get integer data from Redis
        return self.get(key, fn=int)
