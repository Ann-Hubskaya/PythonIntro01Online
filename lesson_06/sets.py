import random
#
# s = set()
# print(type(s), s)
# s = set('Process finished with exit code 0')
# print(type(s), s)
# s = set([4, 6, 'g'])
# print(type(s), s)
# s = {}
# print(type(s), s)
# s = {1}
# print(type(s), s)

# len()
s1 = {random.randint(10, 30) for _ in range(10)}
s2 = {random.randint(10, 30) for _ in range(10)}
print(s1)
print(s2)
#
# # |             union
# s3 = s1 | s2
# print(len(s1), len(s2), len(s3))
# print(s3)
# s3 = s1.union(s2)
# print(s3)
#
# """
# A = A + 4       A += 4
# """
#
# # s1 |= s2
# # s1.update(s2)
#
# # &             intersection()
# # &=            intersection_update()
# s3 = s1 & s2
# print(s3)
# s3 = s1.intersection(s2)
# print(s3)
#
# # -             difference()
# # -=            difference_update()
# s3 = s1 - s2
# print(s3)
# s3 = s1.difference(s2)
# print(s3)

# s3 = s1 - s2
# print(s3)
# print(s1)
# print(s2)
#
# s1.difference_update(s2)
# print(s1)
# print(s2)

# ^             symmetric_difference()
# ^=            symmetric_difference_update()
s3 = s1 ^ s2
print(s3)
s4 = s1 - s2
s5 = s2 - s1
print(s4)
print(s5)
s6 = s4 | s5
print(s6)


s3 = {10, 11, 13, 15, 16, 18, 21, 24, 27, 28, 30}
print(s3)
# remove()
s3.remove(21)
print(s3)

# copy()
s4 = s3.copy()
print(id(s3))
print(id(s4))
print(s4)

# clear()
s3.clear()
print(s3)

# pop()
r = s4.pop()
print(r)
print(s4)

# add()
s4.add(35)
print(s4)
s4.add(18)
print(s4)

for elemen in s4:
    print(elemen, end=' ')
print()

# frozenset
fs = frozenset(s4)
print(type(fs), fs)
s5 = set(fs)
