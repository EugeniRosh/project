"""Прочитать сохранённый csv-файл и сохранить данные в excel-файл,
 кроме возраста - столбец с этими данными не нужен"""

import csv
import openpyxl

with open('csv_file.csv', 'r', encoding='utf=8') as file:
    rows = csv.reader(file)
    book = openpyxl.Workbook()
    sheet = book.active
    num = 1
    for row in rows:
        sheet[f'B{num}'].value = row[0]
        sheet[f'C{num}'].value = row[1]
        sheet[f'D{num}'].value = row[3]
        sheet[f'A{num + 1}'].value = f'Persona {num}'
        num += 1
    book.save('xlsx_file.xlsx')
    book.close()
