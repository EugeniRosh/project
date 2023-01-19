import random

random_number = random.randint(0, 10)

while True:
     number_1 = int(input('Угадайте число от 0 до 10: '))
     if random_number == number_1:
          print('Верно')
          break
     else:
          print('Попробуйте еще раз')
