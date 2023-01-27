"""Модуль проверяющий возможнось перевода строки в число"""


def analyzing(num: str) -> None:
    """Функция проверяющая возможнось перевода строки в число"""
    if num.isdigit():
        print(f'Вы ввели целое положительное число: {int(num)}')
    elif num.replace('-', '', 1).isdigit():
        print(f'Вы ввели целое отрицательное число: {int(num)}')
    elif num.replace('.', '', 1).isdigit():
        print(f'Вы ввели дробное положительное число: {float(num)}')
    elif num.replace('-', '', 1).replace('.', '', 1).isdigit():
        print(f'Вы ввели дробное отрицательное число: {float(num)}')
    else:
        print(f'Вы ввели не корректное  число: {num}')


analyzing(input('Введите число: '))
