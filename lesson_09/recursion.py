# 2 ^ 5 = 2 * 2 * 2 * 2 * 2
# 32 => 2 * 16 => 2 * 8 => 2 * 4 => 2 * 2 => 2 * 1 => 1


def i_pow(base, exp):
    res = 1
    while exp > 0:
        res *= base
        exp -= 1
    return res


def r_pow(base, exp):
    if exp == 0:
        return 1

    return base * r_pow(base, exp-1)


print(i_pow(2, 5))
print(r_pow(2, 5))


#  0   1   1   2   3   5   8   13  21  34  55  89
#  0   1   2   3   4   5   6   7   8   9   10  11


def i_fib(n):
    x1 = 0
    x2 = 1
    res = 0
    while n > 1:
        res = x1 + x2
        x1 = x2
        x2 = res
        n -= 1

    return res


def r_fib(n):
    if 0 <= n <= 1:
        return n

    return r_fib(n-2) + r_fib(n - 1)


print(i_fib(11))
print(r_fib(2))