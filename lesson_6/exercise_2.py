def factorial_calculation(func: int) -> int:
    if func == 1:
        return 1
    else:
        return func * factorial_calculation(func - 1)

factorial = factorial_calculation(int(input('Введите целое число для расчета факториала: ')))

print(factorial)

