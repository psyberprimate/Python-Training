

class Kettle(object):
    
    power_source = "electricity"

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.on = False


    def switch_on(self):
        self.on = True

    def switch_off(self):
        self.on = False


kenwood = Kettle("Kenwood", 8.99)
print(f"{kenwood.name} {kenwood.price}")

hamilton = Kettle("Hamilton", 14.99)
print(f"{hamilton.name} {hamilton.price}")


print(f"Models: {kenwood.name} {kenwood.price} {hamilton.name} {hamilton.price}")


print("Models: {0.name} = {0.price}, {1.name} = {1.price}".format(kenwood, hamilton))


hamilton.switch_on()
print(hamilton.on)
Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_off()
print(hamilton.on)
print(kenwood.on)


print("*" * 80)
kenwood.power = 1.5
print(kenwood.power)

print("Switch to atomic power source")
Kettle.power_source = "atomic"
kenwood.power_source = "shit"
print(Kettle.power_source)
print(hamilton.power_source)
print(kenwood.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)