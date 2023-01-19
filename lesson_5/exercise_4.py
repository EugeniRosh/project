'''''
Неправильно понятое условие)
'''''
#sum_1 = 0                      #TODO рассчитывает сумму кубов символов, а не промежутка чисел

#num_1 = [int(i) for i in str(input('Введите число: '))]

#for i in num_1:
#        sum_1 += i**2

#print(sum_1)

'''''
Через while
'''''

num_2 = int(input('Введите целое цисло: '))

sum_2 = 0

while num_2 > 0:
    sum_2 += num_2**2
    num_2 -= 1

print(sum_2)

'''''
Через for
'''''

num_3 = int(input('Введите целое цисло: '))

sum_3 = 0

for i in range(1, num_3 + 1):
        sum_3 += i ** 2

print(sum_3)


