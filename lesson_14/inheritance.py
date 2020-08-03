
class WaterBird:
    def __init__(self, name):
        self.name = name
        print('Bird is {}'.format(self.name))

    def where_is_live(self):
        print('On the Earth')

    def swim(self):
        print('Can swim fast')

    def voice(self):
        pass


class Penguin(WaterBird):
    def __init__(self, name):
        WaterBird.__init__(self, name)
        print('Penguin is ready!')

    def where_is_live(self):
        print('North Pole')

    def run(self):
        print('Run fast')

    def voice(self):
        print('pi-pi-pi')


class Duck(WaterBird):
    def __init__(self, name):
        super().__init__(name)
        print('Duck is ready')

    def where_is_live(self):
        print('Anywhere')

    def fly(self):
        print('Fly very high')

    def voice(self):
        print('kra-kra-kra')


p = Penguin('Ping')
p.where_is_live()
p.swim()
p.run()
p.voice()
print('=' * 20)
d = Duck('Donald Dug')
d.where_is_live()
d.swim()
d.fly()
d.voice()