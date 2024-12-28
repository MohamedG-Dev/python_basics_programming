class Car:
    wheels=4

    def __init__(self):
        self.name="Benz"
        self.color="Blue"
c1=Car()
c2=Car()
c2.name="Nexon"
c2.color="Gray"
print(c1.name,c1.color,c1.wheels)
print(c2.name,c2.color,c2.wheels)
Car.wheels = 5
print(c1.name,c1.color,c1.wheels)
print(c2.name,c2.color,c2.wheels)
