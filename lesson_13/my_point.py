
class MyPoint:
    def __init__(self, X=0, Y=0):
        self.x = X
        self.y = Y

    def show(self):
        print('X =', self.x)
        print('Y =', self.y)

    def show_self(self):
        return self


pt1 = MyPoint(3, 5)
print(hex(id(pt1)), pt1.show_self())
# print(pt1.x, pt1.y)
pt1.show()
pt2 = MyPoint(7, 1)
print(hex(id(pt2)), pt2.show_self())
# print(pt2.x, pt2.y)
pt2.show()

pt3 = MyPoint()
print(hex(id(pt3)), pt3.show_self())
# print(pt3.x, pt3.y)
pt3.show()
