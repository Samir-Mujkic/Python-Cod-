class Duck(object):

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on it, the watets lovely")

    def quack(self):
        print("Quack quack")

class Penguin(object):

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on it, the watets lovely")

    def quack(self):
        print("Quack quack")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()

if __name__ == "__main__":
    donald = Duck()
    test_duck(donald)

    percy = Penguin()
    test_duck(percy)