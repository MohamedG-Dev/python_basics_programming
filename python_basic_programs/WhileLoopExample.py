#loops Example - While Loop
i=0
while i < 10:
    print("hello")
    i+=1

#sum of first n number
value = int(input("Enter the number to find it's sum:"))
sum=0
i=0
while i<=value:
    sum+=i
    i+=1
print("The sum is:{}".format(sum))