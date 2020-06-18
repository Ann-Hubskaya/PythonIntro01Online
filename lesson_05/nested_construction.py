""""""


"""
                     j
         0  1  2  3  4  5  6  7  8
      0  *  *  *  *  *  *  *  *  *
      1  *  *        *        *  *
      2  *     *     *     *     *
      3  *        *  *  *        *
   i  4  *           *           *
      5  *        *  *   *       *
      6  *     *     *     *     *
      7  *  *        *        *  *
      8  *  *  *  *  *  *  *  *  *
"""

# for _ in range(9):
#     print('*  ' * 9)

size = 11
for i in range(size):
    for j in range(size):
        if i == 0 or i == size-1 or j == 0 or j == size-1 or i == j or i == size - 1 - j or i == size // 2 or j == size // 2:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()

h = 10
w = 12
for i in range(h):
    for j in range(w):
        if i == 0 or i == h-1 or j == 0 or j == w-1:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()