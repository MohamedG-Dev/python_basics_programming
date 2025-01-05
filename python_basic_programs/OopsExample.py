"""
Oops - Object oriented programming structure

What is a class?
- class can be defined as a blueprint/template which describes the state/behavior of its object.
class <class_name>:
    Statements
"""
class Car:
    color = "blue"
    name = "benz"
    def color_car(self,color):
        print("This is a function to see the color of the car - {}".format(color))
    def name_car(self,name):
        print("This is a function for the name of the car - {}".format(name))

car = Car()
car.color_car("Black")
car.name_car("Nexa")
