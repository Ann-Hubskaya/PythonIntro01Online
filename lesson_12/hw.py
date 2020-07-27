from string import ascii_uppercase, ascii_lowercase
from string import digits

from random import randint

print(ascii_uppercase)

s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(ascii_uppercase[2])

print(ascii_lowercase)

print(digits)

s = digits + ascii_uppercase
print(s)

rows = 8
cols = 10

lst = [[randint(10, 80) for _ in range(cols)] for _ in range(rows)]
print(lst)

print(lst[0])
print(lst[0][1])

for i in range(len(lst)):
    for j in range(len(lst[i])):
        print('{:>3}'.format(lst[i][j]), end='')
    print()
print()















