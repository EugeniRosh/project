"""Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные. Создать
файл и записать в него первые 2 строки и закрыть файл. Затем открыть файл на
редактирование и дозаписать оставшиеся 2 строки. В итоговом файле должны быть 4
строки, каждая из которых должна начинаться с новой строки"""


strok_1 = 'Первая строка'
strok_2 = 'Вторая строка'
strok_3 = 'Третья строка'
strok_4 = 'Четвертая строка'


with open('text_file.txt', 'w', encoding='utf=8') as file:
    file.write(f'{strok_1}\n')
    file.write(f'{strok_2}\n')

with open('text_file.txt', 'r', encoding='utf=8') as file:
    print(file.read())

with open('text_file.txt', 'a', encoding='utf=8') as file:
    file.write(f'{strok_3}\n')
    file.write(f'{strok_4}\n')

with open('text_file.txt', 'r', encoding='utf=8') as file:
    print(file.read())

