

class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on it, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()     

class Penguin(object):

    def __init__(self):
        self._wing = Wing(.5)

    def walk(self):
        print("Waddle, I waddle, Waddle")

    def swim(self):
        print("Come on in, there's very cool here")

    def quack(self):
        print("Are you leaving or not")        

    def fly(self):
        self._wing.fly()

if __name__=='__main__':
    donald = Duck()
    donald.fly()

    percy = Penguin()
    percy.fly()