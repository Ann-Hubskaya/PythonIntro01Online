
# [3, 7, 9, 10, 16, 16, 26, 27, 28, 29, 38, 38, 39, 40, 40, 47, 51, 54, 60, 63, 64, 67, 68, 71, 71, 74, 82, 82, 98, 100]
# key = 26

from random import randint

lst = [randint(1, 100) for _ in range(30)]
print(lst)


def bubble_sort(my_lst):
    for i in range(len(my_lst) - 1):
        flag = True
        for j in range(len(my_lst) - 1 - i):
            if my_lst[j] > my_lst[j+1]:
                my_lst[j], my_lst[j+1] = my_lst[j+1], my_lst[j]
                flag = False

        if flag:
            break


def binary_search(my_lst, key, left_idx=0, right_idx=None):
    if right_idx is None:
        right_idx = len(my_lst)

    middle = (left_idx + right_idx) // 2
    while my_lst[middle] != key and left_idx <= right_idx:
        if key > my_lst[middle]:
            left_idx = middle + 1

        if key < my_lst[middle]:
            right_idx = middle - 1

        middle = (left_idx + right_idx) // 2

    return (True, middle) if not (left_idx > right_idx) else (False, middle + 1)


bubble_sort(lst)
print(lst)

key = int(input('Please enter key: '))

res = binary_search(lst, key)


if not res[0]:
    lst.insert(res[1], key)
    print(lst)
else:
    print(res)


