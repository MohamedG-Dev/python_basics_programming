
class MethodOverRidingBase:
    def __init__(self):
        print("base class constructor")
    def a(self):
        print("inside base class")

class MethodOverridingDerived(MethodOverRidingBase):
    def __init__(self):
        super().__init__()
        print("child class constructor")
    def a(self):
        super().a()
        print("inside the derived class")

obj1 = MethodOverridingDerived();
obj1.a()