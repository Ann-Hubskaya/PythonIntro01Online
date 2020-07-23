
# raise ValueError('Not correct type of value')


def set_value(value):
    if value < 1 or value > 10:
        raise ValueError('Value must in range from 1 to 10')


# set_value(14)

# assert
a = 5

assert a > 5, 'a <= 5'

