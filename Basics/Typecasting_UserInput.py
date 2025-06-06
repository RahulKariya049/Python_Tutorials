a = "27"
b = "3"
print(a + b)

# Explicit Typecasting
a = int(a)
b = int(b)
print(a + b)

# implicit Typecasting
c = 8
d = 1.450
e = c + d  # e is implicitly typecasted into float automatically
print(e, type(e))

# input() function is used to take input from user and by default it will take input in form of str
num1 = int(input("Enter a Number: "))
num2 = int(input("Enter another Number: "))
print("The Sum of two numbers are: ", num1 + num2)

num3 = int(input("Enter another Number: "))
print("The Square of Number", num3, "is:", num3 * num3)