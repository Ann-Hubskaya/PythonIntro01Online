
from random import randint
import sys


#                           0       size-1
def quick_sort(my_list, first_idx, last_idx):
    if first_idx >= last_idx:
        return

    i, j = first_idx, last_idx
    middle_value = my_list[(first_idx + last_idx) // 2]

    while i <= j:
        while my_list[i] < middle_value:
            i += 1

        while my_list[j] > middle_value:
            j -= 1

        if i <= j:
            my_list[i], my_list[j] = my_list[j], my_list[i]
            i, j = i+1, j-1

    quick_sort(my_list, first_idx, j)
    quick_sort(my_list, i, last_idx)


# lst = [randint(1, 100) for _ in range(30)]
# print(lst)
# quick_sort(lst, 0, len(lst)-1)
# print(lst)

print(sys.getrecursionlimit())
sys.setrecursionlimit(55555)
print(sys.getrecursionlimit())
