'''''
Тут написано
'''''
number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))

if number_1 >10 and number_2 > 10:
    print('Оба числа больше 10')
elif number_1 > 10 or number_2 > 10:
    print('Одно из чисел больше 10')
else:
    if not bool(number_2):
        print(not bool(1))       #TODO not bool(1) 0 или пустая строка
    else:
        print(not bool(0))       #TODO not bool(0) не 0 и не пустая строка
