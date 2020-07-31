
"""
class ClassName(parent1, parent2 .... parentN):
    body of this class
"""


class Human:
    human_type = 'mammal'
    age = 25
    height = 180
    weight = 85
    phone = '333-65-22'
    address = 'Odessa'


human1 = Human()
print(human1.age)
human1.age = 26
print(human1.age)

human2 = Human()
print(human1.height)
print(human2.height)
print(human2.age)

print(id(human1))
print(id(human2))
