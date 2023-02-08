"""Модуль подсчитывающий количество букв в тексте не зависимо от регистра"""
with open('text.txt', 'r', encoding='utf=8') as file:
    text = file.read()


def letter_count(letter: str) -> None:
    counter = 0
    for i in range(len(text)):
        if letter.lower() == text[i] or letter.upper() == text[i]:
            counter += 1
    print(f'Результат: буква встречается {counter} раза в тексте.')


letter_count(input('Введине латинскую букву: '))
