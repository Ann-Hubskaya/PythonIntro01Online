
"""
for var in iter_obj:
    operator 1
    operator 2
    .
    .
    .


for _ in iter_obj:
    operator 1
    operator 2
    .
    .
    .
"""

# i = 1
#
# for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
#     print('#', i, ' color of rainbow is ', color, sep='')
#     i += 1
#
#
# for i in 1, 2, 3, 'one', 'two', 'three', 5.6, True:
#     print(i)

# for ch in 'D:\PROJECT\Python\HILLEL\PythonIntro01Online\venv\Scripts\python.exe':
#     print(ch, end='-')
# # print('Test')
# print()

# range(start, stop, step)
# range(stop)
# print(range(1, 10, 1))
#
# s = 'D:\PROJECT\Python\HILLEL\PythonIntro01Online\venv\Scripts\python.exe'
# for idx in range(len(s)):
#     print(s[idx], end='-')
# print()

# for i in range(1, 101, 2):
#     print(i, end=' ')
# print()
#
# i = 1
# while i < 101:
#     print(i, end=' ')
#     i += 2

n = int(input('Please enter start: '))
m = int(input('Please enter stop: '))
s = 0
for i in range(n, m+1):
    s += i

print(s)

