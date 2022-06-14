from base_models import BaseStorage, BaseRequest


class Store(BaseStorage):
    __capacity_default = 100
    __items = {}

    def __init__(self, capacity: int = __capacity_default):
        self.__capacity = capacity
        self.__items = {}

    def add(self, name, count):
        if 0 < self.get_free_space <= self.__capacity:
            for k in self.__items.keys():
                if name == k:
                    self.__items[k] = self.__items[k]+count
                    break
            else:
                self.__items.update({name: count})
                print("Товар добавлен")
        else:
            print("Нет места, только %s" % self.get_free_space)

    def remove(self, name, count):
        if 0 <= self.get_free_space <= self.__capacity:
            for k in self.__items.keys():
                if name == k:
                    self.__items[k] = self.__items[k]-count
                if self.__items[k] == 0:
                    self.__items.pop(k, None)
                    print("Товар Удален")
        else:
            print("Нет на складе")

    @property
    def get_free_space(self):
        return int(self.__capacity) - sum(self.__items.values())

    @property
    def get_items(self):
        return self.__items

    @property
    def get_unique_items_count(self):
        return len(self.__items)


class Shop(Store):
    def __init__(self, limit: int = 5):
        super().__init__()
        self.__limit = limit

    @property
    def items_limit(self):
        return self.__limit

    @items_limit.setter
    def items_limit(self, limit):
        self.__limit = limit

    def add(self, name, count):
        if self.get_unique_items_count < self.__limit:
            super().add(name, count)
        else:
            print(f'товар не может быть добавлен')


class Request(BaseRequest):
    def __init__(self, str_):
        lst = self.__get_info(str_)
        self.from_ = lst[4]
        self.to = lst[6]
        self.amount = int(lst[1])
        self.product = lst[2]

    def __get_info(self, str_: str):
        return str_.split(" ")

    def __repr__(self):
        return f"Доставить {int(self.amount)} {self.product} из {self.from_} в {self.to}"
