class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)  # call to parent constructor
        self.grade = grade


s = Student("Riya", 9)
print(s.name)   # Inherited from Person
print(s.grade)  # From Student
