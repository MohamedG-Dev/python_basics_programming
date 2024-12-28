"""
Set is similar to list.
Set can store different types of values/objects.such as string, int, boolean, float,etc
Set cannot store duplicate values
set are defined using curley braces{}
Set is a collection of unordered and un indexed.
"""
S1={"selenium","Cypress","Appium",100,True,100.23,100}#though 100 is added but set will not store it.
print(type(S1))
print(S1)
print(len(S1))
for i in S1:
    print(i)

S1.add('API')
print(S1)

S1.remove("Cypress")#remove() method will throw an error, if the cypress value is unavailable in the set.
print(S1)
S1.discard("API")#discard() method will not throw any error, the values matches with the set then it'll remove else it will not.
print(S1)
#copy a set
s3=S1.copy()
S1.clear()
print(s3)
print(S1)


"""
Following operations are not feasible in Set
#Repetition operation
Concatenation operation
Membership
Iteration
"""