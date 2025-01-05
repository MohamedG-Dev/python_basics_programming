"""
Exception/Errors
Exception are simply disruptions to the flow of program
"""

"""
Try and Except
    try:
        {------}
    except:
        {------}
"""

try:
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))
    c = a / b  # 1/0 -> ZeroDivisionError: division by zero
    print("The result is: {}".format(c))
    print("Ending")
except (ZeroDivisionError,ValueError):#Exception types:ZeroDivisionError,ValueError
    print("please enter a valid number")
else:
    print("inside an else block")
finally:
    print("I am always executed")

print("this is outside try and except block")

#Exception Hierarchy
"""
BASE Exception
    Exception
        1.Attribute Exception/Error
        2.Arithmetic Exception/Error
            a.ZeroDivision Error
            b.FloatingPoint Error
            c.Overflow Error
        3.EOF Exception (End Of File)
        4.Name Exception
    System Exit
    Generator Exit
    Keyboard Interrupt
    
"""
# print(sd) #NameError: name 'sd' is not defined