"""Module for working with data from a file"""
from data_access import (
    dictreader_file_csv500,
    append_file_csv500,
    writer_file_csv500,
    reader_file_csv500,
    ErrorAlreadyExists,
    validate_update_company,
    validate_symbol_data,
    validate_name_data,
    validate_sector,
    )
from functools import wraps
from faker import Faker
from random import choice, uniform

fake = Faker()
dict_cache = {}


def cache(func):
    """Query Cache Detector and Cache Creator"""
    @wraps(func)
    def wrapper(request):
        global dict_cache
        if dict_cache.get(request) is not None:
            print(dict_cache.get(request))
        else:
            dict_cache.setdefault(request, func(request))
            return func(request)
    return wrapper


@cache
def find_info_by_name(company: str) -> list:
    companies = []
    for row in dictreader_file_csv500():
        if company.lower() in row['Name'].lower():
            companies.append({
                'Name': row.get('Name'),
                'Symbol': row.get('Symbol'),
                'Sector': row.get('Sector'),
                'Stock price': row.get('Price')
                }
            )
    return companies


@cache
def get_all_companies_by_sector(sector: str) -> list:
    company = []
    for row in dictreader_file_csv500():
        if sector.lower() in row['Sector'].lower():
            company.append(row['Name'])
    return company


def calculate_average_price() -> None:
    all_price = 0
    counter = 0
    for row in dictreader_file_csv500():
        all_price += float(row.get('Price'))
        counter += 1
    all_price = all_price / counter
    return all_price


def get_top_10_companies() -> None:
    top_10 = []
    rows_sort = sorted(
        dictreader_file_csv500(),
        key=lambda item: float(item['Price']),
        reverse=True
    )
    for row in rows_sort[:10]:
        top_10.append((row['Name'], row['Price']))
    return top_10


def add_new_company(symbol, name, sector, price: str) -> None:
    try:
        validate_symbol_data(symbol)
    except ErrorAlreadyExists as err:
        print(err)
        return

    try:
        validate_name_data(name)
    except ErrorAlreadyExists as err:
        print(err)
        return

    try:
        validate_sector(sector)
    except ErrorAlreadyExists as err:
        print(err)
        return

    company = {
        'Symbol': symbol,
        'Name': name,
        'Sector': sector,
        'Price': price,
    }
    new_company = {}
    key_set = set(list(company) + reader_file_csv500())
    for i in key_set:
        new_company.setdefault(i, company.get(i, 'None'))
    append_file_csv500(new_company)


def update_company_name(symbol, name: str) -> None:
    try:
        validate_update_company(symbol)
    except ErrorAlreadyExists as err:
        print(err)
        return

    new_file = []
    for row in dictreader_file_csv500():
        if symbol.lower() == row.get('Symbol').lower():
            row['Name'] = name
            new_file.append(row)
        else:
            new_file.append(row)
    writer_file_csv500(new_file)


def delete_company(symbol: str) -> None:
    new_file = []
    for row in dictreader_file_csv500():
        if symbol.lower() == row.get('Symbol').lower():
            continue
        else:
            new_file.append(row)
    writer_file_csv500(new_file)


def populate_file_with_random_data(number: str) -> None:
    sector = []
    new_company = {}
    new_file = []
    for _ in range(8):
        sector.append(fake.country())

    for _ in range(int(number)):
        company = {
            'Symbol': fake.company_suffix().upper(),
            'Name': fake.company(),
            'Sector': choice(sector),
            'Price': uniform(0, 500),
        }
        key_set = set(list(company) + reader_file_csv500())
        for i in key_set:
            new_company.setdefault(i, company.get(i, 'None'))
        new_file.append(new_company)
        new_company = {}
    writer_file_csv500(new_file)


def truncate_all(func):
    writer_file_csv500(func)
