try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That's not a valid number.")
else:
    print("Everything worked! Result:", result)
finally:
    print("This will run no matter what.")
