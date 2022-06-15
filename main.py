from models import Shop, Request, Store
from typing import Optional, Dict

if __name__ == '__main__':
    магазин = Shop()
    склад = Store()
    склад.add("печеньки", 15)
    склад.add("собачки", 25)
    склад.add("коробки", 35)

    print()
    qst = Request("Доставить 3 печеньки из склад в магазин")
    print(qst)
    склад.remove(qst.product, qst.amount)

    print(f'Курьер везет {qst.amount} {qst.product} со {qst.from_} в {qst.to}')
    магазин.add(qst.product, qst.amount)
    print(f'Курьер доставил {qst.amount} {qst.product} в {qst.to}')

    print("\nВ склад хранится:\n")

    for items in склад.get_items:
        print(склад.get_items[items], items)

    print("\nВ магазин хранится:\n")

    for items in магазин.get_items:
        print(магазин.get_items[items], items)

    print()
    qst = Request("Доставить 4 печеньки из склад в магазин")
    print(qst)
    склад.remove(qst.product, qst.amount)
    print(f'Курьер везет {qst.amount} {qst.product} со {qst.from_} в {qst.to}')
    магазин.add(qst.product, qst.amount)
    print(f'Курьер доставил {qst.amount} {qst.product} в {qst.to}')

    print("\nВ склад хранится:\n")

    for items in склад.get_items:
        print(склад.get_items[items], items)

    print("\nВ магазин хранится:\n")

    for items in магазин.get_items:
        print(магазин.get_items[items], items)

    #
    #
    # print(qst)
    # print(qst.from_)
    # print(qst.to)
    # print(qst.amount)
    # print(qst.product)

