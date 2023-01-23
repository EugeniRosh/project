list_1 = [1, 2, 1, 5, 26, 5, 1, 2, 26, 8, 1, 5]

dict_1 = {}


def func(spisoc: list) -> dict:
    for i in spisoc:
        v = spisoc.count(i)
        dict_1.setdefault(i, v)
    return dict_1

dict_1 = func(list_1)

print(dict_1)








