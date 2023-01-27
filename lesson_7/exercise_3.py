"""Модуль выводит слова палиндромы из представленного кортежа слов"""


words = ('deed', 'dog', 'peep', 'good', 'enter', 'deified')

#print(tuple(filter(lambda x: x == x[::-1], words)))          #одной строкой

palindroms = tuple(filter(lambda x: x == x[::-1], words))

print(palindroms)
