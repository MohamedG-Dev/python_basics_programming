#Operators
#1.Arithmetic Operators
a=10
b=5
print(a+b)#Addition
print(a-b)#Subtraction
print(a*b)#Multiplication
print(a/b)#Division
print(a%b)#Modulus
print(a**b)#Exponential Operator(power)
print(a//b)#floor division

#2.Comparison Operator
print('------Comparison Operator---------')
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)

str1="cat"
str2="dog"
print('---------------')
print(str1>str2)
print(str1>=str2)
print(str1<str2)
print(str1<=str2)
print(ord('d'))
print(ord("c"))


#Relational Operator Chaining
print('------Relational Operator Chaining---------')
print(10<20<30<40)#o/p: True
print(10>20<30<40)#o/p: False
print('--------Equality operators--------------')
#3. Equality Oeprator
a=10
b=20
print(a==b)
print(a!=b)

print(1==True)
print(0==True)
print(0==False)
print(10==10.0)
print("Apple2Apple"=="Apple2Apple")

#4.Logical Operators
print('--------Logical operators--------------')
print(True and True)
print(1 and 0)

"""
    And Operator logic:
    a. if the value of x, evaluates to False, then the result value is the value of x
    b. if the value of x, evaluates to True, the the result value is the value of y
"""
print(10 and 20)
print(0 and 20)
print(10 or 20)
print(0 or 20)

print(not True)
print(not False)

a==10
print(not a == 10)

#5.Bitwise Operator
"""
1.Bitwise And ($)
2.Bitwise Or (|)
3.Bitwise XOR (^)
4.Bitwise complement(~)
"""
print('--------Bitwise &operator--------------')
print(bin(16))
print(bin(18))
print(16 & 18)
print('--------Bitwise |operator--------------')
print(16|18)
print('--------Bitwise ^(XOR)operator--------------')
#if both the bits are different in nature then the result is 1 else 0
print(16^18)
print('--------Bitwise ~(NOT)operator--------------')
print(~(-4))

"""
6. Shift Operators
    a.Left shift operators(<<)
    b.Right shift operators(>>)
"""
print('--------Shift operator-Left Shift--------------')
print(bin(10))
print(0b101000)
print(10<<2)
print('--------Shift operator-Right Shift--------------')
print(10>>2)
"""
7.Assignment Operators -> =,+=,-=,*=,/=
"""
print('--------Assignment Operators--------------')
x=10
print(x)
x+=10
print(x)
x-=10
print(x)
x*=10
print(x)
x/=10
print(x)

# Python does not support increment and decrement operators
#print(x++) - error

"""
8.Ternary Operator - Conditional operator
    There is no specific keyword or symbol for the ternary operator
    Syntax -> var = first value if condition else second value
"""

a=10
b=20
c=30 if(a>b) else 40
print(c)
"""
a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
min_number= a if(a<b) else b
print(min_number)
"""

"""
9.Identity Operators
    a. is
    2. is not
    a is not b, return true only when two reference var are pointing to the same object
"""
print("-------Identity Operators-------------")
a=10
b=10
print(a is b)
print(a is not b)

"""
10.Membership operator
    1. in
    2. not in
"""
print("--------Membership operators-----------")
a=[10,20,30,35,37,45,50,52,21,60,"abcd"]
print(10 in a)#true
print(20 not in a)#false
print(23 not in a)#true
print(34 in a)#false
