"""
3 types of access modifiers - public,private and protected
By default all the variables and methods are :
public -
protected - _var, def _method(). The scope members are within the class and within the derived class.
private - __varibalename,__methodname. The scopr of the variables or methods are within that class alone
"""
class Car:
    public_var = 9
    _protected_var = 10
    __private_var = 11

    def __init__(self):
        print("Inside Car constructor")

    def public_method(self):
        print("Inside Car public method")

    def _protected_method(self):
        print("Inside protected method")

    def __private_method(self):
        print("Inside private method")
