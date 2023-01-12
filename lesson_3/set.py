set_1 = ['hello', 'daddy', 'mum', 'hello']

print(set_1)

set_2 = set('heLloworLd')

print(set_2)

set_3 = {'a', 'b', 'b', 'd', 'e', 'hello', 'hello', 'world', 'dog'}

print(set_3)

set_3.add('z')

set_3.update('hello')

set_3.add(1)

print(set_3)

set_3.discard(1)

print(set_3)

set_3.remove('b')

set_3.difference_update('hello')

print(set_3)

print(set_3.pop())

print(id(set_3))

print(set_3)

set_3.clear()

print(set_3)
