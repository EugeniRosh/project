text = input('Напишите что-нибудь: ')

text_even = text[1::2]         # цикл вывода начиная с 1 индекса
text_odd = text[0::2]          # цикл вывода с 0 индекса

print(text, end='\n\n')
print(text_even, text_odd, sep='     ', end='\n!!!')


