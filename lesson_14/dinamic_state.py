
class SomeClass:
    pass


def square_method(self):
    return self.x ** 2


def init(self, x):
    self.x = x


SomeClass.new_attr = 45
print(SomeClass.new_attr)

SomeClass.init = init
SomeClass.square_method = square_method
obj = SomeClass()
obj.init(34)
print(obj.square_method())