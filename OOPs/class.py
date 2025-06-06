a = 456
class Employee:
    # a = 478
    language = "Python" #These are class Attributes 
    Salary = 1200000

#Object declaration or
#Class instantiation
user = Employee()
user.name = "Rahul" #Object attribute
print(user.name, user.language, user.Salary)
print(a)

user2 = Employee()
user2.name = "Lodu"
user2.language = "Java" #object attribute is preffered over class attribute
print(user2.name, user2.language, user2.Salary)