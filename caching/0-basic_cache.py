#!/usr/bin/python3
"""
BasicCaching
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Implements a basic cache by extending the BaseCaching class.
    """

    def put(self, key, item):
        """ add element to dict of cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get element of dict by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
