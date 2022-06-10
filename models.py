from abc import ABC

from base_models import BaseStorage


class Store(BaseStorage):
    __capacity_default = 100
    __items = {}

    def __init__(self, capacity: int = __capacity_default):
        self._capacity = capacity

    def add(self, name, count):
        pass

    def remove(self):
        pass

    @property
    def get_free_space(self):
        return Store.__capacity_default - self._capacity

    @property
    def get_items(self):
        return Store.__items

    @property
    def get_unique_items_count(self):
        return set(Store.__items.keys())
