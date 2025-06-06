# lambda arguments: expression

# Takes arguments
# Returns the value of the expression (no return keyword needed)

square = lambda x: x * x
print(square(5))  # Output: 25



# 2️⃣ Higher-Order Functions
# Functions that:

# Take other functions as arguments, or

# Return functions as results

nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)  # Output: [1, 4, 9, 16, 25]

# Here, map() is a higher-order function because it takes a function (lambda x: x**2) as input.

nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # Output: [2, 4, 6]

# Creating Your Own Higher-Order Function
def apply_func(f, value):
    return f(value)

print(apply_func(lambda x: x + 10, 5))  # Output: 15
