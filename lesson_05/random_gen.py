import random

"""
random.random
random.randint
random.randrange
random.uniform
"""

# random.random()       0 - 1
for _ in range(15):
    print(round(random.random(), 2), end='  ')
print()

# random.randint(start, stop)  from START to STOP
for _ in range(15):
    print(random.randint(10, 50), end='  ')
print()

# random.randrange(start, stop, step)   from START to STOP by STEP
for _ in range(15):
    print(random.randrange(11, 50, 2), end='  ')
print()

# random.uniform(start, stop)       from START to STOP
for _ in range(15):
    print(round(random.uniform(11, 50), 2), end='  ')
print()
