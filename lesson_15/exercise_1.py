class Contact:
    def __init__(self, email, phone, first_name, last_name):
        self.email = email
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name

    def _validator_name(self, value):
        if not value[0].isupper():
            raise ValueError(
                f'Name "{value}" should start from capital letter.'
                )

        if len(value) not in range(5, 16):
            raise ValueError(f'Name "{value}" lenght must be 5-15 simbol.')

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        value_split = value.split('@')
        if len(value_split) != 2:
            raise ValueError('email must contain one @.')

        if value_split[1] not in (
                            'gmail.com',
                            'yandex.ru',
                            'ya.ru',
                            'yahoo.com'
                            ):
            raise ValueError('Unsupported email provider.')

        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if value[:4] not in ('+375', '+374'):
            if value[:3] != '+48':
                raise ValueError('Invalid phone country codes')

        self._phone = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._validator_name(value)

        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._validator_name(value)

        self._first_name = value
