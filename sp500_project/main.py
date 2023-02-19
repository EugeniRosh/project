"""Module providing information to the user"""
from business_logic import (
   find_info_by_name,
   get_all_companies_by_sector,
   calculate_average_price,
   get_top_10_companies,
   add_new_company,
   update_company_name,
   delete_company,
   populate_file_with_random_data,
   truncate_all,
    )
from validators import (
    validate_choice,
    validate_name_company_choice,
    validate_price,
    validate_number_of_generated_companies,
    validate_symbol,
    )
from errors import IncorrectUserInputError

while True:
    print(
        '1 - Find info by name', '2 - Get all companies by sector',
        '3 - Calculate average price', '4 - Get top 10 companies',
        '5 - Add new company', '6 - Update company name',
        '7 - Delete company', '8 - Truncate all',
        '9 - Populate file with random data', '10 - Exit', sep='\n'
    )

    choice = input('Your choice: ')

    try:
        validate_choice(choice)
    except IncorrectUserInputError as err:
        print(err)
        continue

    if int(choice) == 1:
        company_name = input('Enter the name of company: ')
        companies = find_info_by_name(company_name)
        if companies is None:
            continue
        print(f'Companies with the name: {company_name}', *companies, sep='\n')

    elif int(choice) == 2:
        sector_name = input('Enter the name of sector: ')
        company = get_all_companies_by_sector(sector_name)
        if company is None:
            continue
        print(f'Companies in the sector: {sector_name}', *company, sep='\n')

    elif int(choice) == 3:
        print(f'Average share price: {calculate_average_price()}')

    elif int(choice) == 4:
        top_10 = get_top_10_companies()
        print('Top 10 companies: ', *top_10, sep='\n')

    elif int(choice) == 5:
        symbol = input('Enter company symbol: ')
        try:
            validate_symbol(symbol)
        except IncorrectUserInputError as err:
            print(err)
            continue

        name = input('Enter company name: ')
        try:
            validate_name_company_choice(name)
        except IncorrectUserInputError as err:
            print(err)
            continue

        sector = input('Enter company sector: ')

        price = input('Enter company price: ')
        try:
            validate_price(price)
        except IncorrectUserInputError as err:
            print(err)
            continue

        add_new_company(symbol, name, sector, price)

    elif int(choice) == 6:
        symbol = input('Enter company symbol: ')

        name = input('Enter new company name: ')
        try:
            validate_name_company_choice(name)
        except IncorrectUserInputError as err:
            print(err)
            continue

        update_company_name(symbol, name)

    elif int(choice) == 7:
        symbol = input('Enter the company symbol to delete it: ')
        delete_company(symbol)

    elif int(choice) == 8:
        truncate_all('')

    elif int(choice) == 9:
        number = input('Enter the number of entries to create: ')
        try:
            validate_number_of_generated_companies(number)
        except IncorrectUserInputError as err:
            print(err)
            continue
        populate_file_with_random_data(number)

    elif int(choice) == 10:
        print('GOODBAY')
        break
