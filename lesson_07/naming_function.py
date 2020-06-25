# print("Сколько бананов и ананасов для обезьян?")
# a = int(input())
# b = int(input())
# print("Всего", a * b, "шт.")
#
# print("Сколько жуков и червей для ежей?")
# a = int(input())
# b = int(input())
# print("Всего", a * b, "шт.")
#
# print("Сколько рыб и моллюсков для выдр?")
# a = int(input())
# b = int(input())
# print("Всего", a * b, "шт.")

"""
def function_name():
    body
"""


def animals_food(food_1, food_2):
    return food_1 + food_2


# d = print("Сколько рыб и моллюсков для выдр?")
# print(d)
# a = int(input("Рыба"))
# b = int(input("Молюски"))
# res = animals_food(a, b)
# print("Всего", res, "шт.")
#
# print("Сколько жуков и червей для ежей?")
# # ввод из файла
# print("Всего", animals_food(a, b), "шт.")
#
# animals_food(a, b)

# x = 6
#
#
# def some_func():
#     global x
#     x = 8
#     # x = x + 6
#     y = 7
#     print(x, y)
#
#
# some_func()
# print(x)


# Ключевые параметры или параметры по умолчанию
# def my_print(msg, times=1):
#     print(msg * times)
#
#
# my_print("test ")
# my_print("test ", 4)
#
#
# def func(a, b, c, d=1, e=2, f=3):
#     pass
#
#
# func(3, 5, 7)
# func(3, 4, 5, 6)
# func(3, 4, 5, 6, 1)
# func(3, 4, 5, 6, 1, 9)
#
#
# def func1(a, b, c, d=111, e=222, f=333):
#     print('a = {A}\tb = {B}\tc = {C}\td = {D}\te = {E}\tf = {F}\n'.format(
#         A=a, B=b, C=c, D=d, E=e, F=f
#     ))
#
#
# func1(3, 5, 7)
# func1(3, 4, 5, 6)
# func1(3, 4, 5, 6, 1)
# func1(3, 4, 5, 6, 1, 9)
#
# func1(c=30, d=34, a=10, b=20)


# *args и **kwargs - функции с переменным числом аргументов


# print(1)
# print(1, 2)
# print(1, 2, 3)


def func2(*args):
    print(type(args), args)
    for value in args:
        print(value, end=' ')
    print()


func2(3, 5, 7)
func2(3, 4, 5, 6)
func2(3, 4, 5, 6, 1)
func2(3, 4, 5, 6, 1, 9)

a = 5, 6, 7, 6
print(type(a), a)


def func3(a, b, c):
    a += 3
    b *= 4
    c /= 2
    return a, b, c


x = func3(4, 6 ,8)
print(type(x), x)

q, w, e = 1, 2, 3
x1, y1, z1 = func3(4, 6 ,8)
print(x1, y1, z1)
