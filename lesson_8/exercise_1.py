"""Декодировать в строку байтовое значение: b'r\xc3\xa9sum\xc3\xa9'. Затем
результат преобразовать в байтовый вид в кодировке ‘Latin1’ и затем результат
снова декодировать в строку (результаты всех преобразований выводить на экран)"""


strok = b'r\xc3\xa9sum\xc3\xa9'

becod_strok = strok.decode('utf-8')
print(becod_strok)

strok_latina1 = becod_strok.encode('Latin1')
print(strok_latina1)

decod_latin1 = strok_latina1.decode('Latin1')
print(decod_latin1)

