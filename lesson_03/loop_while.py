"""
while
for
"""

"""
while <condition>:
    operator1
    expression
else:
    operator1
    
"""

i = 1
while i <= 10:
    i += 1
    print(i)

"""
break
"""
while True:
    print('In loop')
    break


# x = 0
# while x < 10:
#     y = int(input("Enter a number: "))
#     if y > 25:
#         break
#
#     print('x =', x, 'y =', y)
#     x += 0.1
# else:
#     print('Block else')

"""
continue
"""

# a = 1
# b = 1
while True:
    a = int(input('Введите делимое: '))
    if a == 0:      # if not a:
        break
    b = int(input('Введите делитель: '))
    if b == 0:      # if not b:
        print('Делить на 0 нельзя:', a)
        continue
    print(a / b)
