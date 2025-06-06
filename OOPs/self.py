class Employee:
    language = "Python" #These are class Attributes 
    Salary = 1200000

    def get_info(self):
        print(f"The User name is {self.name}, language used ny developer is {self.language}, and Salary is {self.Salary}")

    #this function doesn't needs to get whole object as parameter so we made it static method
    @staticmethod
    def greet():
        print("Good Morning...!!!")

user = Employee()
user.name = "Rahul" #Object attribute

user.get_info()
#This Function Call is same as
# Employee.get_info(user)

user.greet()