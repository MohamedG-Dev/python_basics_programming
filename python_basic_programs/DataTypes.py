import random

x=10
print(type(x))
print(isinstance(x,int))
x=11.1
print(type(x))
print(isinstance(x,int))
x=5j
print(type(x))
x="abcd"
print(type(x))
x=True
print(type(x))
x=["one","two","three"]
print(type(x))
x=("four","five","six")
print(type(x))
x={"seven","eight","nine"}
print(type(x))
x=frozenset({"ten","eleven","twelve"})
print(type(x))
x={"firstname":"rahul","lastname":"arora"}
print(type(x))

print(2*2*2*2)
print(2**4)#** -> represents power 2^4 = 16

x=-11223344122131134123451092342
print(type(x))

#random method
print(random.randrange(1,20))

print(10>5)#prints the value as true
print(10<5)#prints the value as false
print(10==5)#prints the value as false

#pi in python
from math import pi
print(pi)
print(type(pi))

print(3.111111111111111111199) #this takes/prints the value only upto range 15 after the decimal

print(10/2)#this will give the result in decimal value
print(10//2)#this will give the result in integer value

print(10%3)#output is 1
print(5/2)
print(5//2)