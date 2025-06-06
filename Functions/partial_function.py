# You have a generic function, but often use it with some common values.
# You want to avoid repeatedly passing the same arguments.
# You want to integrate functions cleanly into pipelines like map(), filter(), etc.
#Basic Example

from functools import partial

def multiply(x, y):
    return x * y

# Create a new function that always multiplies by 2
double = partial(multiply, 2)

print(double(5))  # Output: 10
print(double(10)) # Output: 20
#double = partial(multiply, 2) freezes the first argument x = 2.

#Use in map()
from functools import partial

def power(base, exponent):
    return base ** exponent

# Create a square function by fixing exponent=2
square = partial(power, exponent=2)

nums = [1, 2, 3, 4]
print(list(map(square, nums)))  # Output: [1, 4, 9, 16]
