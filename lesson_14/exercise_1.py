class Alphabet:
    def __init__(self, end, lower=True):
        self.end = end
        self.lower = lower

    def __iter__(self):
        if self.lower:
            self.start = 97
            self.finish = ord(self.end.lower())
        else:
            self.start = 65
            self.finish = ord(self.end.upper())

        return self

    def __next__(self):
        if self.start > self.finish:
            raise StopIteration

        result = self.start

        self.start += 1

        return chr(result)


for letter in Alphabet(end="z"):
    print(letter)
