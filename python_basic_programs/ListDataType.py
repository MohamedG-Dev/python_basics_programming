"""
List Data is a consecutive collection of all the related items
List represents group of values as single entity, order/sequence of items inside the list is very important
It allows duplicate values as well
It represented by a square bracket []
values are separated by commas(,)

"""
a=[]#empty list
b=[1,2.3,"Thomas",True,3+2j,"Thomas",2.3]
print(type(b))
print(b)
"""
propeties of List
1.order of list is preserved
2.list allows duplicate values
3.list is mutable in nature -i.e size of the list is not fixed. we can add any number of values to the list
"""
print(b[2])
print(b[5])
b.append("Shelby")
print(b)#o/p: [1, 2.3, 'Thomas', True, (3+2j), 'Thomas', 2.3, 'Shelby']
emp=[101,"Thomas","India"]
dep1=["IT",10]
dep2=["EEE",12]
print(f"Name is {emp[1]} and the employee id is {emp[1]} and the location is {emp[2]}")

#List slicing
print('-------------List slicing----------------')
c=[0,1,2,3,4,5,6]
print(c[0:])#o/p:[0, 1, 2, 3, 4, 5, 6]
print(c[:])#o/p:[0, 1, 2, 3, 4, 5, 6]
print(c[2:4])#o/p:[2, 3]
print(c[:4])#o/p:[0, 1, 2, 3]

#Updating list values
print('----------updating list--------')
d=[1,2,3,4,5,6,7]
print(d)
d[2]=7
print(d)
d[1:4]=["Thomas","Shelby",100]
print(d)
#Deleting values from the list
print('-----delete a value from the list-----------')
del d[4]
print(d)#o/p:[1, 'Thomas', 'Shelby', 100, 6, 7]
print(len(d))#o/p: 6

#sorting the list
print('-----------sorting the list--------')
e=["e","f","a","d","b","c"]
print(e)
e.sort()#ascending sorting
print(e)
e.sort(reverse=True)#descending sorting
print(e)

"""
List Operations
1.Repetition operation
2.Concatenation operation
3.Membership operation
4.Iterations
5.Length Function
"""
print('-------List Operation- Repetitive--------')
l1=[1,2.2,"Three",True]
l1=l1*2
print(l1)
print('-------List Operation- Concatenation--------')
l2=[4,5,6,"seven",False]
print(l1+l2)
print('-------List Operation- Membership--------')
print("Three" in l1)
print("seven" not in l2)
print('-------List Operation- Iteration--------')
for i in l1:
    print(i)

print(len(l1))
print(len(l2))

l3=[1,2,3,4,5,6,7,8,9]
print(max(l3))
print(min(l3))

string = "Rahul"
print(list(string))
