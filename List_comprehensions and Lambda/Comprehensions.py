#  1. List Comprehensions
squares = [x**2 for x in range(10) if x % 2 == 0]

# Set Comprehensions
unique_lengths = {len(word) for word in ["apple", "banana", "cherry", "apple"]}


# Dictionary Comprehensions
squares_dict = {x: x**2 for x in range(5)}

# Nested Comprehensions
# Syntax:
# [expression for sublist in outer_list for item in sublist]

# Example:
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]