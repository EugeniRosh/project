lisr_1 = []
print(lisr_1)

lisr_1.append(1)
lisr_1.append(2)
print(lisr_1)

lisr_1.insert(1, 8)
print(lisr_1)
print(lisr_1[0])

lisr_1.pop(2)
print(lisr_1)

lisr_1.extend('752')     #добоаляет только итерабельные элеиенты
print(lisr_1)            #разбивая на символы

lisr_1.pop(4)
print(lisr_1)
lisr_1.pop(3)
print(lisr_1)
lisr_1.pop(2)
print(lisr_1)

lisr_1.append(2)
lisr_1.append(8)
lisr_1.append(55)

lisr_1.sort()            #не работает если есть int и str
print(lisr_1)

lisr_1.sort(reverse=True)
print(lisr_1)

lisr_1.clear()
print(lisr_1)
