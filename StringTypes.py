print("This is a String")

a="hello world"
print(a)
print(type(a))

a='String Types'
print(a)
print(type(a))

'''
The line 11 which has 3 apostrophe
can be used as a multiple
line of comments in pyhton
'''
print('Hey, How are you "Shane"')

a = "Hey"\
"My Name Is"\
"Rahul"
print(a)

b="""
Hey
My Name is:
Thomas Murphy
"""
print(b)

print("Thomas's new book name is \"Dear Life's Bucket\"")

book="legacy"
print(book[0])
print(book[5])
print(book[1:4])#slicing a string. output is - ega
print(book[1:5:1])#last value 1 indicates jumping 1 step at a time. o/p is egac
print(book[1:5:2])#last value 2 indiciates jumping 2 step at a time. o/p is ea
print(book[::])#this will print the string as it is
print(book[::2])#the output of this is lgc
print(book[1::2])#output is: eay
print(book[::-1])#this reverse the string. o/p: ycagel
print(len(book))

name="  Hello, this is Rahul    "
print(name)
print(name.strip())#This strip method will remove the white spaces from the front as well from the back
b=name.split(",")
print(b[0].strip())
print(b[1].strip())

name="BreakingBad"
print(name.lower())
print(name.upper())

str1 = "Hello"
str2 = " Thomas Shelby"
print(str1+str2)

# print(5+"5")#unsupported operand type error

#repition of Strings
print("10"*3)#output: 101010
print("ba"+"na"*2)#output: banana i.e. na gets repeated(multiplied na*na) and gives the output as banana. it applies bodmas rule

#String formatter
city = "Chennai"
print("Hey, I live in ",city)

#f-String formatter
age = 33
id = 1010
print(f"Hey, I live in {city}, my age is {age} and my id is {id}")

#format()
print("Hey, I live in {}, my age is {} and my id is {}".format(city, age, id))

#% String formatter
bal=3.456
print("Hey, I live in %s, my age is %d and my balance is %f"%(city,age,bal))