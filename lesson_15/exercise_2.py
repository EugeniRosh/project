from time import time


class Censored:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        value_split = value.split()
        for i in range(len(value_split)):
            if value_split[i].lower() == 'fuck':
                value_split.pop(i)
                value_split.insert(i, '****')
                value = ' '.join(value_split)

        setattr(instance, self.name, value)


class Message:
    text = Censored()

    def __init__(self, text):
        self.text = text
        self.created_at = time()


class Song:
    name = Censored()

    def __init__(self, name, autor):
        self.name = name
        self.autor = autor
        self.created = time()
