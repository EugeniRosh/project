"""Модуль переводит лист типа данных int в лист типа данных str"""


list_int = [i for i in range(1, 15)]     #для практики

list_str = list(map(lambda x: str(x), list_int))

print(list_str)

#print(list(map(lambda x: str(x), [i for i in range(1, 15)])))   # одной строкой
