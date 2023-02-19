"""File handling module"""
import csv


class ErrorAlreadyExists(Exception):
    ...


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


def validate_update_company(symbol: str) -> None:
    symbol_value = set()
    for row in dictreader_file_csv500():
        symbol_value.add(row.get('Symbol').lower())

    if symbol.lower() not in symbol_value:
        raise ErrorAlreadyExists(
            'The input character is not in the file'
            )


def validate_symbol_data(symbol):
    for row in dictreader_file_csv500():
        if symbol.lower() == row.get('Symbol').lower():
            raise ErrorAlreadyExists(
                'A company with this symbol already exists.'
                )


def validate_name_data(name):
    for row in dictreader_file_csv500():
        if name.lower() == row.get('Name').lower():
            raise ErrorAlreadyExists(
                'A company with this name already exists.'
                )


def validate_sector(sector) -> None:
    sector_value = set()
    for row in dictreader_file_csv500():
        sector_value.add(row.get('Sector'))

    if sector not in sector_value:
        raise ErrorAlreadyExists('Wrong sector name.')
