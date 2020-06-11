"""
if <condition>:
    operator 1
    operator 2
else:
    operator 3
    operator 4

operator 5
"""

a = 6

if a > 10:
    print('a more then 10')
else:
    print('a less then 10')

# if a < 10:
#     print('a less then 10')

print('after operator if')

b = '5'

if b > '0':
    print('positive')
elif b < '0':
    print('negative')
else:
    print('zero')


"""
x = A ? B : C
"""

A = 15
B = 3
C = 9
#     если      иначе
x = B if A > 10 else C

print(x)







