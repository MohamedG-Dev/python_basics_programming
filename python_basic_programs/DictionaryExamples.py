"""
Dictionary
1. stores key and value pairs
    a. key - represents is Numbers, strings, tuples
    b. value - Python object
"""
D1={
    "Name":"Thomas",
    "Age":35
}
print(type(D1))#o/p: <class 'dict'>
print(D1)#{'Name': 'Thomas', 'Age': 35}

D2={
    "Name":"Thomas",
    "Age":35,
    "Salary":12000.20,
    "Organization":"Shelby Limited",
    "is_Married":True
}
print("Name - {}".format(D2["Name"]))
print("Age - {}".format(D2["Age"]))
print("Salary - {}".format(D2["Salary"]))
print("Organization - {}".format(D2["Organization"]))
print("Is Married - {}".format(D2["is_Married"]))
#Update a Dictionary
"""
print("-------Update a dictionary----------")
D2["Name"]=input("Enter name:")
D2["Age"]=int(input("Enter age:"))
D2["Salary"]=float(input("Enter Salary:"))
D2["Organization"]=input("Enter Organization:")
D2["is_Married"]=bool(input("Are you married?:"))
print(D2)
"""
print('-------Delete a key from the dictionary------')
del D2["is_Married"]
print(D2)

print('-----Iterate over a dictionary--------')
#printing all key values
print('-------printing all keys from dictionary-----------')
for i in D2:
    print(i)

#printing all values
print('-------printing all the values alone from the dictionary-----------')
for i in D2:
    print(D2[i])

print('--------printing all the values using values()method----------')
for i in D2.values():
    print(i)

print('--------printing the key and values in the form of tuple----------')
for i in D2.items():
    print(i)
print('------------Another Example of Dictionary---------')
item={
    "fruits":["Apple","Banana","Mango"],
    "price":100,
    "size":10.5
}

print(item["fruits"])
print(item["fruits"][0])

print('----Dictionary inside a dictionary----------')
item1={
    "location":"India",
    "fruits":{"Name":"Guava","Price":101}
}
print(item1)
print(item1["fruits"]["Name"])
print(item1["fruits"]["Price"])
print(type(item1.get("location")))
print(type(item1.get("fruits")))
print(type(item1.get("fruits").get("Price")))
print(item1.get("fruits").get("Price"))
print(len(item1))
print(item1.keys())
print('------iterating over item1 dictionary using .keys() method-> to get keys from the dictionary------')
for i in item1.keys():
    print(i)