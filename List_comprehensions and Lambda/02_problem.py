from functools import reduce
#  Problem: Salary Processing System
# You are given a list of employee records in the following format:

data = [
    "Alice,₹90,000",
    "Bob,₹1,20,000",
    "Charlie,₹70,000",
    "Daisy,₹1,10,000"
]
# Write a one-liner using map() and reduce() to calculate the total salary of all employees.

# ⚠️ Conditions:
# You must clean the currency symbol and commas.
# Use map() to transform the salaries into integers.
# Use reduce() to sum them up.

total_salary = reduce(lambda x, y: x + y , list(map(lambda x: int(x.split(',₹')[1].replace(',','')), data)))
print(total_salary)