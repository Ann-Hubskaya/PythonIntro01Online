# List
import random

a = []
print(type(a), a)
a = list()
print(type(a), a)
a = list('Hello World!')
print(type(a), a)
a = [2, 5, 54, 7, 4, 'RYER', 45.65, True]
print(type(a), a)

print(a[3])
# print(a[19])
print(a[2:6])

print(a * 2)

b = list('Hello World!')
print(a + b)

# in
print(25 in (a+b))
print('H' in (a+b))
print(25 not in (a+b))
print('H' not in (a+b))

# append()
lst = []
for _ in range(25):
    lst.append(random.randint(10, 50))
print(lst)

# min(), max(), sum()
print(min(lst))
print(max(lst))
print(sum(lst[4: 10]))

# index(value, start)
# print(lst.index(12))

# count(value)
print(lst.count(12))

# pop(), pop(index)
print(lst.pop())
print(lst)

print(lst.pop(1))
print(lst)

# insert(index, value)
lst.insert(0, 888)
print(lst)

# clear()
# lst.clear()
# print(lst)

# copy()
print(id(lst), lst)
a = lst
print(id(a), a)
a = lst.copy()
print(id(a), a)

# extend(list)
x1 = lst[: 10]
x2 = a[-10:]
print(x1)
print(x2)
x3 = x1 + x2
x1.extend(x2)
print(x1)

# remove(value)
print(lst)
lst.remove(12)
print(lst)

# del
del lst[1]
print(lst)

# reverse()
lst.reverse()
print(lst)

b = lst[::-1]

z = []
for i in range(1, 100):
    z.append(i)
print(z)





