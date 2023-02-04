"""Прочитать соранённый json-файл и записать данные на диск в csv-файл, первой
строкой которого озоглавив каждый столбец и добавив новый столбец "телефон"."""

import csv
import json

with open('json_file.json', 'r', encoding='utf=8') as file:
    contents = json.load(file)

columns = ['id', 'name', 'age', 'phone number']

phone = [{'phone number': 256587},
         {'phone number': 527866},
         {'phone number': 520505},
         {'phone number': 885987},
         {'phone number': 785966},
         {'phone number': 484441}]

ind = 0
for k, v in contents.items():            # соединили данные json_file.json и переменной phone
    phone[ind].update({columns[0]: k, columns[1]: v[0], columns[2]: v[1]})
    ind += 1

with open('csv_file.csv', 'w', newline='', encoding='utf=8') as file:
    writerdict = csv.DictWriter(file, fieldnames=columns)
    writer = csv.writer(file)
    writer.writerow(columns)
    writerdict.writerows(phone)

with open('csv_file.csv', 'r', encoding='utf=8') as file:
    rows = csv.DictReader(file)
    for row in rows:
        print(row)


