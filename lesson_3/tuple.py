tuple_1 = (1, 2, 3, 4, 5, 5, 5,)

print(tuple_1.count(5))

print(tuple_1.index(3))

print(tuple_1.index(5))

print(tuple_1)

print(id(tuple_1))

list_1 = list(tuple_1)

list_1.append(10)

tuple_1 = tuple(list_1)

print(tuple_1)

print(id(tuple_1))

tuple_2 = tuple('1252')

print(tuple_2)

tuple_3 = tuple((1,))

print(tuple_3)
