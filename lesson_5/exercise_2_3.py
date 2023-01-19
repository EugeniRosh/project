while True:
    name = input('Введите ваше имя: ')

    age = input('Введите ваш возраст: ')

    age_1 = int(age) if bool(1) == age.isdigit() else 1       # .isdigit проверяет возможнось перевода str в int

    if age_1 <= 0 or bool(0) == age.isdigit():
        print('Ошибка повторите ввод')

    elif 0 < age_1 < 10:
        print(f'Привет шкет {name.title()}!')

    elif 10 <= age_1 <= 18:
        print(f'Как жизнь {name.title()}?')

    elif 18 < age_1 < 100:
        print(f'Что желаете {name.title()}?')

    else:
        print(f'{name.title()}, вы лжете - в наше время столько не живут...')




