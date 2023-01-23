dict_1 = {'dog': 'cat', 'blue': 'green', 'big': 'small'}

print(dict_1)

dict_2 = {}


def func(name_func: dict) -> dict:
    for k, v in name_func.items():
        dict_2.setdefault(v, k)
    return dict_2


dict_2 = func(dict_1)

print(dict_2)
