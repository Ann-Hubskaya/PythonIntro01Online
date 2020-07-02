# yield


def count_down_1(num):
    result = []
    while num != 0:
        result.append(num - 1)
        num -= 1
    return result


print(count_down_1(5))


# for i in range(10 ** 10):
#     if i > 4:
#         break

def count_down_2(num):
    while num != 0:
        yield num - 1
        num -= 1


# for i in count_down_2(10):
#     if i == 5:
#         break
#
#     print(i)


it = count_down_2(5)
print(type(it), it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))

print()

lst = [4, 3, 2, 1, 0]
it2 = iter(lst)
print(type(it2), it2)
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
