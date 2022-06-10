from abc import ABC, abstractmethod


class BaseStorage(ABC):

    @property
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @property
    @abstractmethod
    def add(self, *args, **kwargs):
        pass

    @property
    @abstractmethod
    def remove(self, *args, **kwargs):
        pass


    @property
    @abstractmethod
    def get_free_space(self):
        pass

    @property
    @abstractmethod
    def get_items(self):
        pass

    @property
    @abstractmethod
    def get_unique_items_count(self):
        pass


class BaseRequest(ABC):

    @property
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

