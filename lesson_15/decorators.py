# from datetime import datetime


def measure_time(func):
    from datetime import datetime

    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper


@measure_time
def gen_1(arg):
    lst = []
    # start = datetime.now()
    for i in range(arg):
        if i % 2 == 0:
            lst.append(i)
    # print(datetime.now() - start)
    return lst


@measure_time
def gen_2(arg):
    # start = datetime.now()
    lst = [x for x in range(arg) if x % 2 == 0]
    # print(datetime.now() - start)
    return lst


res = len(gen_1(10 ** 5))
print(res)
res = len(gen_2(10 ** 5))
print(res)

# r = measure_time(gen_2)
# print(type(r), r)
# a = r()
# print(type(a), a)
