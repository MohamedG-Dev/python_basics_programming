"""
1.Operator overloading
2.Method overloading and Method overriding
3.constructor overloading and overriding

1.operator overloading
1+2=-1
"""
class OperatorOVerloading:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self, other):
        totalpages = self.pages-other.pages
        return totalpages
obj1=OperatorOVerloading(10)
obj2=OperatorOVerloading(5)
print(obj1+obj2)

#Method overloading - which ever last method comes with the same name gets picked up first to execute.
#i.e. ths current method gets added as recently in the memory
#Hence method overloading is not possible in Python
class MethodOverloading:
    def __init__(self):
        print("Inside the default constructor")
    def __init__(self,name):
        print("Inside the parameterized constructor")
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c

mo=MethodOverloading()
#print(mo.add(10,20))#comment this line and execute the below line for the output without any error
print(mo.add(10,20,30))
mo1=MethodOverloading("Python")
