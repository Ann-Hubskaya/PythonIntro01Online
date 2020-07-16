from random import randint

lst = [randint(1, 100) for _ in range(30)]
print(lst)

key = int(input('Please enter key: '))
for idx in range(len(lst)):
    if lst[idx] == key:
        print('Key {} exists in list'.format(key))
        print('Index of element: {}'.format(idx))
        break
else:
    print('Key {} not exists in list'.format(key))
