"""
Iterative statements
1. For Loop
    Syntax:
    for x in sequence:
        statements
2. While Loop
"""

sequence="legacy"
i=0
for x in sequence:
    print("The character present at {} index is - {}".format(i,x))
    i+=1

for x in range(10):# range give 0 to n-1. i.e. 0 to (10-1) is 0 to 9
    print("Hello Worlds")

for x in range(1,11):#start index is 1 and end index is (11-1)=10
    print(x)

for x in range(2,20,3):
    print(x)

#multiplication example
n = int(input("Enter the number:"))
for x in range(1,11):
    print(n,"*",x,"=",n*x)

#eval is a method that can take any form of inputs from the user. such as list, strings
List = eval(input("Enter the list of numbers to find the sum of them"))
#Enter the list of numbers to find the sum of them[10,20,40,50,60]
sum=0
for x in List:
    sum += x
print("The sum is: ",sum)#The sum is:  180

string = "My Name is Thomas Shelby"
str = string.split(" ")
for x in str:
    print(x)
