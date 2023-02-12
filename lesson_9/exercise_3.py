"""A module that counts the number of letters in a text, regardless of case"""


def letter_count(letter: str) -> None:
    counter = 0
    with open('text.txt', 'r', encoding='utf=8') as file:
        for line in file:
            for i in range(len(line)):
                if letter.lower() == line[i] or letter.upper() == line[i]:
                    counter += 1
        print(f'Результат: буква встречается {counter} раза в тексте.')


letter_count(input('Введине латинскую букву: '))
