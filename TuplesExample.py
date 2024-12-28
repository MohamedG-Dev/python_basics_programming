"""
Tuple can store only immutable objects
mostly all other operations are similar to a list
"""
t1 = ("thomas",29,20.09,True)
print(type(t1))
#t1[2]=40
print(t1)#TypeError: 'tuple' object does not support item assignment

t2=(0,1,2,3,4,5)
print(t2[0:])#(0, 1, 2, 3, 4, 5)
print(t2[:])#(0, 1, 2, 3, 4, 5)
print(t2[2:4])#(2, 3)
print(t2[1:3])#(1, 2)
print((t2[:4]))#(0, 1, 2, 3)

#del t2[3]#Deletion is not possible in tuple
print(t2)

#tuple operations - Repetition,Concatenation,Membership,Iteration
print('----performing tuple operations-------------')
t3=(1,"Thomas")#Repetition operation
print(t3*2)
t4=(2,"Tom")
print(t3+t4)#Concatenation operation
print("Thomas" in t3)#Membership operation
print("Tom" not in t4)#Membership operation
for i in (1,2,3,4,5):#Iteration operation
    print(i)