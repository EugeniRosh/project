"""Модуль соеденяющий 2 списка"""
first_dict = {'a': 1, 'b': 2, 'c': 3}

second_dict = {'c': 3, 'd': 4, 'e': 5}

merged_dict = {}

for k in first_dict.keys():
    for i in second_dict.keys():
        merged_dict.setdefault(k, [first_dict.get(k), second_dict.get(k)])
        merged_dict.setdefault(i, [first_dict.get(i), second_dict.get(i)])

print(merged_dict)
