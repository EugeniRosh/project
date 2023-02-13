"""Прочитать сохранённый csv-файл и сохранить данные в excel-файл,
 кроме возраста - столбец с этими данными не нужен"""

import csv
import openpyxl

with open('csv_file.csv', 'r', encoding='utf=8') as file:
    rows = csv.reader(file)
    book = openpyxl.Workbook()
    sheet = book.active
    num = 0
    for row in rows:
        row.pop(2)
        row.insert(0, f'Persona {num}') if num != 0 else row.insert(0, f'')
        sheet.append(row)
        num += 1
    book.save('xlsx_file.xlsx')
    book.close()
