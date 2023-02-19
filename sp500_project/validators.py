"""Module validating received data"""
from errors import IncorrectUserInputError


def validate_choice(choice: str) -> None:
    if not choice.isdigit():
        raise IncorrectUserInputError('Choice mast be digit.')

    if int(choice) not in [x for x in range(1, 11)]:
        raise IncorrectUserInputError('Choice must be from 1 to 10')


def validate_name_company_choice(name: str) -> None:
    if not 3 <= len(name) <= 50:
        raise IncorrectUserInputError(
            'Name must be between 3 to 50 characters'
            )


def validate_symbol(symbol: str) -> None:
    if not 3 <= len(symbol) <= 6:
        raise IncorrectUserInputError(
            'Symbol must be between 3 to 6 characters'
            )

    for i in symbol:
        if i.isdigit():
            raise IncorrectUserInputError('Should not be digit.')

    if not symbol.isascii():
        raise IncorrectUserInputError(
            'Must contain only uppercase, latin letters'
            )

    if not symbol.isupper():
        raise IncorrectUserInputError('Must contain only capital letters')


def validate_price(price: str) -> None:
    if not price.replace('.', '', 1).replace('-', '', 1).isdigit():
        raise IncorrectUserInputError('Must be a floating point number.')

    if not 1 <= float(price) <= 1000:
        raise IncorrectUserInputError(
            'The price should be in the range from 1 to 1000'
            )


def validate_number_of_generated_companies(number: str):
    if not number.isdigit():
        raise IncorrectUserInputError('The entered character is not a digit')

    if not 1 <= int(number) <= 10000:
        raise IncorrectUserInputError(
            'The price should be in the range from 1 to 10000'
            )
