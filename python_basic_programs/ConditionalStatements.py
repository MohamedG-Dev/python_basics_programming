"""#Python Flow Controls
1. If statement
2. If Else statement
3. If Elif Else statement
4. For loops
5. While loops
6. Nested loops
7. Break statement
8. Continue statement
9. Loop with Else block
10. Pass statement
"""

a=10
b=5
if a>b:
    print(a)
    print("A is greater")
else:
    print(b)
    print("B is greater")
print("outside conditional statements")

marks=int(input("Enter marks:"))
section=input("Enter section:")
if marks==100:
    if section=='A':
        print("Good")
    grade='A++'
    print(grade)
elif 80<marks<100:
    print("B")
elif 60<marks<80:
    print("C")
else:
    print("Student failed")