#!/usr/bin/env python3
"""
Cache class
"""
import functools
from typing import Callable, Optional, Union
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """ decorateur for count many times func is call """
    # Récupération du nom qualifié de la méthode
    key = method.__qualname__

    # Définition du wrapper qui va encapsuler la méthode originale
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper """
        # Incrémentation du compteur associé à la méthode
        self._redis.incr(key)
        # Appel de la méthode originale avec les arguments et les mots-clés
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """ cache class """

    def __init__(self) -> None:
        """ init """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
