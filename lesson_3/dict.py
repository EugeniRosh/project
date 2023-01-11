dict_1 = {}
print(dict_1)

dict_2 = {'dog': 1, 'cat': 2}
print(dict_2)

dict_3 = dict(short = '2')
print(dict_3)

dict_3[12] = 5
print(dict_3)

dict_3['12'] = 8
print(dict_3)

dict_3['12'] = 3
print(dict_3)

dict_4 = {'hi': {'hi': [1, 2, 3, 4]}}
print(dict_4)

print(dict_3.keys())

print(dict_3.items())

dict_3.popitem()
print(dict_3)

dict_3.pop(12)
print(dict_3)

print(dict_3.values())

print(dict_3.clear())