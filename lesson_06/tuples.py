# tuple

t = ()
print(type(t), t)
t = tuple()
print(type(t), t)
t = tuple('Process finished with exit code 0')
print(type(t), t)
t1 = tuple([1, 2, 4, 5, 7, 8])
print(type(t), t)
t2 = 4, 6, 4, 2, 7
print(type(t), t)

t = 5,
print(type(t), t)

t3 = t1 + t2
print(type(t3), t3)

print(t2 * 3)
print(t3[5])

for el in t3:
    print(el, end=' ')

# count()
# index()
# in, not in
# max(), min(), sum()
# len()
print()
lst = list(t3)
lst[5] = 'TEST'
t4 = tuple(lst)
print(t4)
