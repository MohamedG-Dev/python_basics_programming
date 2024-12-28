"""
Single inheritance, Multi level, Multiple inheritance
"""
class AnimalParent:
    def ap(self):
        print("Inside the animal parent class")
class Animal(AnimalParent):
    name="Lion"
    def a(self):
        print("I am inside animal class")

class Mammals(Animal):
    def b(self):
        print("I am inside mammals class")
class Cow(Mammals,Animal):
    def cow(self):
        print("inside the cow class")

mam=Mammals()
mam.b()
mam.a()
print(mam.name)
mam.ap()
cowobject=Cow()
cowobject.ap()
cowobject.a()
cowobject.b()
cowobject.cow()