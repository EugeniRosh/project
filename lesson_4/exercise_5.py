number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))

if number_1 == number_2:
    print(number_1, '=', number_2)
elif number_1 > number_2:
    print(number_1, '>', number_2)
else:
    print('Отработала секция else')