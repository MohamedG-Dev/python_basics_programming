"""
Constructors are called as the first function of the class.
syntax -  __init__
All the classes will have this function which is always executed when the class is being initiated
or an object of the class is created
Note: We cannot overload a constructor
"""
class practice:
    def __init__(self):
        print("Inside constructor")

    def add(self):
        print("performing addition operation")

p=practice()
p.add()

class Employee:

    def __init__(self,name,id):
        self.name = name
        self.id=id
    def display(self):
        print("Name is: ",self.name)
        print("Age is: ",self.id)
e1=Employee("rohan",101)
e1.display()
e2 = Employee("Rakesh",102)
e2.display()