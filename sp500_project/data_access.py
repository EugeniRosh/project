"""File handling module"""
import csv


def dictreader_file_csv500():
    with open('sp500.csv', 'r', encoding='utf=8', newline='\n') as file:
        for row in csv.DictReader(file):
            yield row


def append_file_csv500(new_company):
    with open('sp500.csv', 'a', encoding='utf=8', newline='') as file:
        data = csv.DictWriter(file, fieldnames=reader_file_csv500())
        data.writerow(new_company)


def writer_file_csv500(new_file):
    colomns = reader_file_csv500()
    with open('sp500.csv', 'w', encoding='utf=8', newline='') as file:
        data = csv.DictWriter(file, fieldnames=colomns)
        data.writeheader()
        data.writerows(new_file)


def reader_file_csv500():
    with open('sp500.csv', 'r', encoding='utf=8') as file:
        return list(csv.reader(file))[0]
