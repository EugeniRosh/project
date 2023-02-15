"""Module connecting 2 dict"""
first_dict = {'a': 1, 'b': 2, 'c': 3}

second_dict = {'c': 3, 'd': 4, 'e': 5}

key_set = set(list(first_dict) + list(second_dict))

merged_dict = {}

for k in key_set:
    merged_dict.setdefault(k, [first_dict.get(k), second_dict.get(k)])

print(merged_dict)
