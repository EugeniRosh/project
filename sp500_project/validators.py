"""Module validating received data"""
from errors import IncorrectUserInputError
from data_access import dictreader_file_csv500


def validate_choice(choice: str) -> None:
    if not choice.isdigit():
        raise IncorrectUserInputError('Choice mast be digit.')

    if int(choice) not in [x for x in range(1, 11)]:
        raise IncorrectUserInputError('Choice must be from 1 to 10')


def validate_name_company(name: str) -> None:
    if not 3 <= len(name) <= 50:
        raise IncorrectUserInputError(
            'Name must be between 3 to 50 characters'
            )

    for row in dictreader_file_csv500():
        if name.lower() == row.get('Name').lower():
            raise IncorrectUserInputError(
                'A company with this name already exists.'
                )


def validate_symbol(symbol: str) -> None:
    if not 3 <= len(symbol) <= 6:
        raise IncorrectUserInputError(
            'Symbol must be between 3 to 6 characters'
            )

    for i in symbol:
        if i.isdigit():
            raise IncorrectUserInputError('Should not be digit.')

    if not symbol.isupper():
        raise IncorrectUserInputError('Must contain only capital letters')

    if not symbol.isascii():
        raise IncorrectUserInputError(
            'Must contain only uppercase, latin letters'
            )

    for row in dictreader_file_csv500():
        if symbol.lower() == row.get('Symbol').lower():
            raise IncorrectUserInputError(
                'A company with this symbol already exists.'
                )


def validate_sector(sector) -> None:
    sector_value = set()
    for row in dictreader_file_csv500():
        sector_value.add(row.get('Sector'))

    if sector not in sector_value:
        raise IncorrectUserInputError('Wrong sector name.')


def validate_price(price: str) -> None:
    if not price.replace('.', '', 1).isdigit():
        raise IncorrectUserInputError('Must be a floating point number.')

    if not 1 <= float(price) <= 1000:
        raise IncorrectUserInputError(
            'The price should be in the range from 1 to 1000'
            )


def validate_update_company(symbol: str) -> None:
    symbol_value = set()
    for row in dictreader_file_csv500():
        symbol_value.add(row.get('Symbol').lower())

    if symbol.lower() in symbol_value:
        raise IncorrectUserInputError(
            'The input character is not in the file'
            )
