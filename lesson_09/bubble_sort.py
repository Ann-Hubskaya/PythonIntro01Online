from random import randint

# lst = [randint(1, 100) for _ in range(30)]
lst = [3, 7, 9, 10, 16, 16, 26, 27, 28, 29, 38, 38, 40, 39, 40, 47, 51, 54, 60, 63, 64, 67, 68, 71, 71, 74, 82, 82, 98, 100]
print(lst)

cnt = 0

for i in range(len(lst) - 1):
    flag = True
    for j in range(len(lst) - 1 - i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            flag = False

    cnt += 1

    if flag:
        break

print(cnt)
print(lst)

# [3, 7, 9, 10, 16, 16, 26, 27, 28, 29, 38, 38, 40, 39, 40, 47, 51, 54, 60, 63, 64, 67, 68, 71, 71, 74, 82, 82, 98, 100]
