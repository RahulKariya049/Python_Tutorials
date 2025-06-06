# What is an Exception?
# An exception is an error that occurs during program execution. Instead of crashing, Python lets you handle it gracefully.

# Basic Structure: try / except
# try:
    # Code that might throw an exception
    # risky_operation()
# except SomeError:
#     # Handle the error gracefully
#     print("Something went wrong!")

# 🔹 Common Exception Types:
# Exception	                                Cause
# ZeroDivisionError	                        Dividing by zero
# TypeError	                                Wrong data type operation
# ValueError	                            Invalid value
# IndexError	                            List index out of range
# KeyError	                                Dict key doesn’t exist
# FileNotFoundError	                        File access error
# ImportError	                            Module can’t be imported

# 🧪 Example:

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That's not a valid number.")
