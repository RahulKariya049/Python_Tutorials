class Employee:
    language = "Python" #These are class Attributes 
    Salary = 1200000

    def __init__(self, name, languauge, salary):
        self.name = name
        self.language = languauge
        self.Salary = salary
        print("The Constructor is being called because an object of class Employee is created..")
 
    def get_info(self):
        print(f"The User name is {self.name}, language used ny developer is {self.language}, and Salary is {self.Salary}")

    #this function doesn't needs to get whole object as parameter so we made it static method
    @staticmethod
    def greet():
        print("Good Morning...!!!")

user = Employee("Rahul" , "Python", 120000000)

user.get_info()
