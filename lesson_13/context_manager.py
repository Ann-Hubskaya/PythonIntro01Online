
lst = [
    'Максимальное напряжение, B             > 250',
    'Максимальный ток, А                    > 6',
    'Тип рабочего тока                      > переменный',
    'Высота педали, мм                      > 43.5',
    'Толщина педали, мм                     > 18',
    'Количество контактов (без реверса)     > 6'
]

# file = open('test.txt', 'w')
# for line in lst:
#     file.write(line)
#     file.write('\n')
#
# file.close()
#
# file = open('test.txt')
# for line in file:
#     print(line, end='')
#
# print()
# file.close()

with open('test.txt', 'w') as file:
    for line in lst:
        file.write(line + '\n')

    print("File is close" if file.closed else "File is open")

print("File is close" if file.closed else "File is open")

with open('test.txt') as file:
    for line in file:
        print(line, end='')
    print()
    print("File is close" if file.closed else "File is open")

print("File is close" if file.closed else "File is open")


size_buff = 32

with open('test_sign.jpg', 'rb') as src, open('test_sign_copy.jpg', 'wb') as dst:
    while True:
        data = src.read(size_buff)
        if data:
            dst.write(data)
        else:
            break

