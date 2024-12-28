#Break statement example - used to break the current loop
from operator import itemgetter

for i in range(10):
    if i==7:
        print("executing break at",i)
        break
    print("the index value of i is:",i)
print("Outside the for loop")

#continue state example - It is used to skip the current iteration and continue with the next iteration
print("Printing the Odd numbers")
for i in range(10):
    if i%2==0:
        print("even number is:",i)
        continue
    print("odd number is:",i)

print('------------------------')
for i in range(10):
    if i==7:
        print(i)
        break
    elif i==5:
        continue
    print(i)

#Else block within the Loop
print('-------Else block within loop-----')
cart = [10,20,600,30,40,50,550]
for item in cart:
    if item>500:
        print("This item is not allowed")
        break
    print(item)
else:
    print("All items are successfully processed.....")
print('--------------------------')
for item in cart:
    if item>500:
        print("This item is not allowed")
        continue
    print(item)
else:
    print("All items are successfully processed")

#Pass statement- pass is a null operation — when it is executed, nothing happens.
# It is useful as a placeholder when a statement is required syntactically,
# but no code needs to be executed,
for x in "legacy":
    pass