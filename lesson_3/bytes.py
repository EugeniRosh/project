bytes_1 = b'test'

print(type(bytes_1))

print(bytes_1)

bytes_2 = bytes('привет'.encode())

print(bytes_2)

bytes_3 = bytes('hi'.encode())

print(bytes_3)

#bytes_4 = b'привет'       выдает ошибку не ASCII
#print(bytes_4)

bytes_4 = chr(50)

print(bytes_4)