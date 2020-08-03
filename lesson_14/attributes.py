"""


"""


class Point:
    """
    Class describe point.
    """
    type_point = 'attribute of class'

    def __init__(self, x=0, y=0):
        """

        :param x:
        :param y:
        """
        self.x = x
        self.y = y

    def get_class_attr(self):
        """

        :return:
        """
        return self.__class__.type_point


# pt1 = Point()
# print(pt1.x)
# pt2 = Point(3, 4)
# print(pt2.x)
#
# pt1.x = 7
# print(pt2.x)
#
# print(pt1.type_point)
# print(pt2.type_point)
# # pt1.type_point = 'test pt1'
# # print(pt1.type_point)
# # print(pt2.type_point)
#
# Point.type_point = 'test class Point'
# print(pt1.type_point)
# print(pt2.type_point)


class Triangle:
    def __init__(self, x0, y0, x1, y1, x2, y2):
        self.peak_A = Point(x0, y0)
        self.peak_B = Point(x1, y1)
        self.peak_C = Point(x2, y2)


tr = Triangle(3, 4, 7, 6, 9, 1)
print(tr.peak_B.y)

print(tr.peak_C.get_class_attr())

# __doc__
print(Point.__doc__)
# __name__
print(Point.__name__)
# __dict__
print(Point.__dict__)
# __module__
print(Point.__module__)
# __bases__
print(Point.__bases__)