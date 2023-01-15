"""
Тут что-то написано
"""
# Задание 1
num1 = 1
num2 = 1
num3 = 1
print('Задание 1', id(num1), id(num2), id(num3), end='\n\n')

# Задание 2
list_1 = ['l']
tuple_1 = ('l',)
print('Задание 2', id(list_1), id(tuple_1), end='\n\n')

# Задание 3

num2 = float(num2)
num3 = str(num3)
print('Задание 3/1', id(num1), id(num2), id(num3), end='\n\n')

           # Вариант 1
list_1 = list_1[0]
tuple_1 = tuple_1[0]
print('Задание 3/2v1', id(list_1), id(tuple_1), end='\n\n')

          # Вариант 2
list_2 = ['Hello', 'hi']
set_2 = {'Hello', 'hi'}

list_2 = bool(list_2)
set_2 = bool(set_2)
print('Задание 3/2v2', id(list_2), id(set_2), end='\n\n')

                # Вариант 3              #TODO не работает с буквами и не односимвальными цифрами
list_3 = [9]
set_3 = {9}
list_3 = str(list_3).strip('[]')           #TODO .strip удаляет все символы указанные в ' '
set_3 = str(set_3).strip('{}')
tuple_3 = (9,)
tuple_3 = str(tuple_3).strip('(),')
print('Задание 3/2v3', id(list_3), id(set_3), id(tuple_3), end='\n\n')

                 # Вариант 4
lst = [-5]                                  #TODO начиная с цифры 257 id не совподают, работает в интервале -5 - 256
st = {-5}
lst = int(''.join(map(str, lst)))
st = int(''.join(map(str, st)))
print('Задание 3/2v4', id(lst), id(st))




