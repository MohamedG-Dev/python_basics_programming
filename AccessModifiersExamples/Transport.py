from AccessModifiersExample import Car
car = Car()
print(car.public_var)
print(car._protected_var)
#print(car.__private_var)#this will throw an error
print(car._Car__private_var)

car.public_method()
car._protected_method()
#car.__private_method()#this will throw an error
car._Car__private_method()