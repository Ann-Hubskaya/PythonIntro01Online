string = 'Hello World!'
number = 43897653987264978326
float_num = 454.43542

very_long_name_of_variable = 23423

some_list = [23423, '45645', True, float_num]


def print_list(lst):
    # print('From mod 1')
    for el in lst:
        print(el, end=' ')
    print()

# print(dir())


if __name__ == '__main__':
    print_list(some_list)
    print(__name__)
