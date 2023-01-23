import time

list_1 = []


def timer(func: list) -> list:
    for i in func:
        list_1.append(time.strftime("%m.%d.%Y %H:%M:%S"))
        time.sleep(1)
    return list_1


n = int(input('введите длину списка: '))

timer(i for i in range(1, n))

print(list_1)
