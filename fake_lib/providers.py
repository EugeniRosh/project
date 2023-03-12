from random import randint, choice


class EmailProvider:
    def __call__(self):
        mail = ['@gmail.com', '@yandex.ru', '@ya.ru', '@yahoo.com']
        name_mail = ''.join([
            chr(randint(97, 122)) for _ in range(randint(5, 10))
            ])
        return name_mail + choice(mail)


class PhoneProvider:
    def __call__(self):
        cod_phone = ['+37533', '+37544', '+37529']
        phone = ''.join([
            chr(randint(49, 57)) for _ in range(7)
            ])
        return choice(cod_phone) + phone


class BankCardProvider:
    def __call__(self):
        total = 1
        while total % 10 != 0:
            num = [randint(0, 9) for _ in range(14)]
            num.append(randint(4, 5))
            num_revers = num[::-1]

            for i in range(len(num)):
                if i % 2 == 0:
                    num[i] *= 2
                    if num[i] > 9:
                        num[i] -= 9

            num_revers.append(sum(num) % 10)
            bank_card = ''.join(map(str, num_revers))
            total = 0
            for i in range(len(num_revers)):
                if i % 2 == 0:
                    num_revers[i] *= 2
                    if num_revers[i] > 9:
                        num_revers[i] -= 9
                total += num_revers[i]

        return bank_card


class NameProvider:
    def __call__(self):
        list_name = [
            'Liam', 'Olivia', 'Noah', 'Emma', 'Oliver', 'Charlotte',
            'Elijah', 'Amelia', 'James', 'Ava', 'William', 'Sophia',
            'Benjamin', 'Isabella', 'Lucas', 'Mia', 'Henry', 'Evelyn',
            'Theodore', 'Harper'
            ]

        return choice(list_name)
