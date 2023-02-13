"""Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные. Создать
файл и записать в него первые 2 строки и закрыть файл. Затем открыть файл на
редактирование и дозаписать оставшиеся 2 строки. В итоговом файле должны быть 4
строки, каждая из которых должна начинаться с новой строк"""

line_1 = 'Первая строка'
line_2 = 'Вторая строка'
line_3 = 'Третья строка'
line_4 = 'Четвертая строка'


with open('text_file.txt', 'w', encoding='utf=8') as file:
    file.write(f'{line_1}\n')
    file.write(f'{line_2}\n')

with open('text_file.txt', 'r', encoding='utf=8') as file:
    print(file.read())

with open('text_file.txt', 'a', encoding='utf=8') as file:
    file.write(f'{line_3}\n')
    file.write(f'{line_4}\n')

with open('text_file.txt', 'r', encoding='utf=8') as file:
    print(file.read())

