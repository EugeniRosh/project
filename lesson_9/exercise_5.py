"""Module for working with the sp500.csv file via the console"""
import csv
from functools import wraps


def cache(func):
    """Query Cache Detector and Cache Creator"""
    @wraps(func)
    def wrapper(request):
        global dict_cache
        if dict_cache.get(request) is not None:
            print(dict_cache.get(request))
        else:
            dict_cache.setdefault(request, func(request))
    return wrapper


@cache
def find_info_by_name(company: str) -> list:
    companies = []
    with open('sp500.csv', 'r', encoding='utf=8') as file:
        rows = csv.DictReader(file)
        for row in rows:
            if company.lower() in row['Name'].lower():
                companies.append(row)
        print(f'Companies with the name: {company}', *companies, sep='\n')
    return companies


@cache
def get_all_companies_by_sector(sector: str) -> list:
    company = []
    with open('sp500.csv', 'r', encoding='utf=8') as file:
        rows = csv.DictReader(file)
        for row in rows:
            if sector.lower() in row['Sector'].lower():
                company.append(row['Name'])
        print(f'Companies in the sector: {sector}', *company, sep='\n')
    return company


def calculate_average_price() -> None:
    all_price = 0
    counter = 0
    with open('sp500.csv', 'r', encoding='utf=8') as file:
        rows = csv.DictReader(file)
        for row in rows:
            all_price += float(row['Price'])
            counter += 1
        print(f'Average share price: {all_price / counter}')


def get_top_10_companies() -> None:
    top_10 = []
    with open('sp500.csv', 'r', encoding='utf=8') as file:
        rows = csv.DictReader(file)
        rows_sort = \
            sorted(rows, key=lambda item: float(item['Price']), reverse=True)
        for row in rows_sort[:10]:
            top_10.append((row['Name'], row['Price']))
        print('Top 10 companies: ', *top_10, sep='\n')


dict_cache = {}

while True:
    print('1 - Find info by name')
    print('2 - Get all companies by sector')
    print('3 - Calculate average price')
    print('4 - Get top 10 companies')
    print('5 - Exit')
    choice = input('Your choice: ')
    if int(choice) == 1:
        company_name = input('Enter the name of company: ')
        find_info_by_name(company_name)
    elif int(choice) == 2:
        sector_name = input('Enter the name of sector: ')
        get_all_companies_by_sector(sector_name)
    elif int(choice) == 3:
        calculate_average_price()
    elif int(choice) == 4:
        get_top_10_companies()
    elif int(choice) == 5:
        print('GOODBYE')
        break
    else:
        print('Input Error. Repeat input ')
