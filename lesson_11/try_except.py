
# def div(a, b):
#     res = a / b
#     return res
#
#
# while True:
#     try:
#         x = int(input("Enter A: "))
#         y = int(input("Enter B: "))
#
#         r = div(x, y)
#         print(r)
#     except ZeroDivisionError as ex:
#         print(ex)
#     except ValueError as ex:
#         print(ex)
#     else:
#         print('No error')
#     finally:
#         print('finally')

file = None
try:
    file = open('test.txt', 'w')
    x = int(input("Enter A: "))
    y = int(input("Enter B: "))

    file.write(str(x / y))

except ZeroDivisionError as ex:
    print('Zero division error')
except ValueError as ex:
    print('Value error')
finally:
    if file is not None and not file.closed:
        file.close()
