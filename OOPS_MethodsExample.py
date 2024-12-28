# shortcut key for the comments is ctrl+o+/
"""
Three types of methods/functions
1.Instance method - used to access through the instance of a class
2.Class method - used to access static of the class
3.Static method - standalone method
"""
class Car:
    wheels=4

    def __init__(self):
        self.name="Benz"
        self.color="Blue"
    #instance method
    def get_car_name(self):
        print(self.name)
    #class method
    @classmethod
    def get_car_wheels(cls):
        print(cls.wheels)

    #static method
    @staticmethod
    def general_information():
        print("20% dicount on cars")
c1=Car()
c1.get_car_name()
#c1.get_car_wheels()
Car.get_car_wheels()
Car.general_information()
c2=Car()