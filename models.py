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
            else:
                self.__items.update({name: count})
                print("Товар добавлен")
        else:
            print("Нет места, только %s" % self.get_free_space)

    def remove(self, name, count):
        if 0 < self.get_free_space <= self.__capacity:
            for k in self.__items.keys():
                if name == k:
                    self.__items[k] = self.__items[k]-count
            else:
                self.__items.update({name: count})
                print("Товар Удален")
        else:
            print("Нет на складе")

    @property
    def get_free_space(self):
        return self.__capacity - sum(self.__items.values())

    @property
    def get_items(self):
        return f"Список {self.__items}"

    @property
    def get_unique_items_count(self):
        return len(self.__items)


class Shop(Store):
    def __init__(self, limit: int = 5):
        super().__init__()
        self.__limit = limit

    def add(self, name, count):
        if self.get_unique_items_count < self.__limit:
            super.add(name, count)
        else:
            print(f'товар не может быть добавлен')


class Request(BaseRequest):
    def __init__(self):
        self.from_ = ""
        self.to = ""
        self.amount = 0
        self.product = ""

def get_info(self, str_: str):
    return str_.split(" ")





s1 = Store(100)
s2 = Shop(20)
s1.add('ddd', 5)
s1.add('ddd', 8)
s1.add('ddd4', 10)
s1.remove('ddd4', 30)
s1.remove('ddd4', 40)
s1.remove('ddd4', 40)
# print(s1.get_free_space)
# print(s1.get_items)
# print(s1.get_unique_items_count)
