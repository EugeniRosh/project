"""Модуль выодит время отработки функций"""
from datetime import datetime


def time_interval(x):
    """Декоратор"""
    def wrapper(*args, **kwargs):
        """функция считает время отработки функций"""
        total = 0
        for _ in range(100):
            start = datetime.timestamp(datetime.now())
            x(*args, **kwargs)
            end = datetime.timestamp(datetime.now())
            total = total + (end - start)
        print(f'Среднее время {round(total/100, 10)} секунд')
    return wrapper


dict_1 = {'dog': 'cat', 'blue': 'green', 'big': 'small'}

@time_interval
def func_1(name_func: dict) -> dict:
    """Функция меняет местами ключ: значение в словаре"""
    dict_2 = {v: k for k, v in name_func.items()}
    return dict_2


list_1 = [1, 2, 1, 5, 26, 5, 1, 2, 26, 8, 1, 5]
dict_2 = {}


@time_interval
def func_2(spisoc: list) -> dict:
    """Функция проверяющая количество одинаковых чисел в списке и выдающая число: количество в виде словаря"""
    for i in spisoc:
        v = spisoc.count(i)
        dict_2.setdefault(i, v)
    return dict_2


func_1(dict_1)
func_2(list_1)