num = int(input('Please enter a number: '))

# 123       ==>   1     2    3

# a = num % 10
# b = num // 10 % 10
# c = num // 100
#
# print(a, b, c, sep='')
#
# res = a * 100 + b * 10 + c
# print(res)

res = 0
while num > 0:
    res = res * 10 + num % 10
    num //= 10

print(res)
