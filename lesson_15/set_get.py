class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __get_x(self):
        return self.__x

    def __set_x(self, x):
        self.__x = x

    def __del_x(self):
        self.__x = 0

    def __get_y(self):
        return self.__y

    def __set_y(self, y):
        self.__y = y

    def __del_y(self):
        self.__y = 0

    x = property(__get_x, __set_x, __del_x, '')
    y = property(__get_y, __set_y, __del_y, '')


point = Point(2, 4)
# print(point.x)
# point.x = 9
# print(point.x)
# print(point._Point__x)
# point._Point__x = 9

# print('X =', point._Point__get_x())
# print('Y =', point.get_y())
# point.set_x(6)
# point.set_y(8)
# print('X =', point.get_x())
# print('Y =', point.get_y())

# print(point.x)
# point.x = 5
# print(point.x)
# del point.x
# print(point.x)


class PointD:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @x.deleter
    def x(self):
        self.__x = 0

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @y.deleter
    def __del_y(self):
        self.__y = 0


point = PointD(2, 4)
# print(point.x)
# point.x = 9
# print(point.x)
# print(point._Point__x)
# point._Point__x = 9

# print('X =', point._Point__get_x())
# print('Y =', point.get_y())
# point.set_x(6)
# point.set_y(8)
# print('X =', point.get_x())
# print('Y =', point.get_y())

print(point.x)
point.x = 5
print(point.x)
del point.x
print(point.x)



