def print_company_name():
    print("Shelby Company limited")

print_company_name()

def print_shelby_name(name):
    print("Shelby Company Name is: "+name)
print_shelby_name("Thomas Shelby Limited")

def print_thomas_sister_name(name):
    return "Thomas sister Name is: "+name
print(print_thomas_sister_name("Ada"))
sister_name = print_thomas_sister_name("Ada Shelby")
print(sister_name)

def get_user_details(name,age,salary):
    print("Name is: "+name,",the age is: "+str(age)+" and the salary is: "+str(salary))
    print("Name is:",name,",the age is:",age,"and the salary is:",salary)
get_user_details("John Shelby",29,100000)
get_user_details(salary=2300000,name="Arthur Shelby",age=39)#Keyword arguments - the keyword has to same as the name of the parameter name.
#this can change the order but with the parameter names, and
# it's argument values can pick it up and assign it to the right parameter with its value

"""
Types of Arguments
1.Required Arguments
2.Keyword Arguments
3.Default Arguments
4.Variable length Arguments
"""

def requirement_arguments(a,b):
    return a+b
print(requirement_arguments(2,4))

def default_argument(name,company_name="Shelby limited"):
    print("Name- {}".format(name))
    print("Company Name- {}".format(company_name))

default_argument("Finn Shelby")
default_argument("Polly gray","Gray Limited")
default_argument(company_name="Press Conference",name="Ada Shelby")

def variable_length_argument(company_name,*name):#by default, it is a tuple
    print(company_name)
    for i in name:
        print(i)

variable_length_argument("Shelby Limited","Thomas","Ada","Polly","John","Arthur",12,2.234,True)