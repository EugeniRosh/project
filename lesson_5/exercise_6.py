import timeit

file = open('text.txt', 'w')

age = '25'

file.write(str(timeit.timeit("x = sum([1, 2, 100, 200, 500])")) + '\n')

file.write(str(timeit.timeit('x = sum([1, 2, 100, 200, 500])', number = 15)) + '\n')

file.write(str(timeit.timeit('age_1 = int(age) if bool(1) == age.isdigit() else 1', globals=globals(), number=3)) + '\n')

file.close()

with open('text.txt', 'r') as file:
    print(file.read())

