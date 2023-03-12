import providers


class FakeFactory:
    def __init__(self, provider, number):
        self.provider = provider()
        self.number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if not isinstance(value, int):
            raise ValueError('Number must by digit.')

        if not value > 0:
            raise ValueError('Number must by > 0.')

        self._number = value

    def generate(self):
        return self.provider()

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == self._number:
            raise StopIteration

        self.counter += 1

        return self.provider()


ff = FakeFactory(providers.BankCardProvider, 10)
