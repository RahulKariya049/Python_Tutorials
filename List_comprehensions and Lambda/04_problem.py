# You have this list of employee records:
from functools import reduce
employees = [
    ("Alice", 28, "HR", 60000),
    ("Bob", 34, "IT", 85000),
    ("Charlie", 25, "Finance", 72000),
    ("Daisy", 40, "IT", 90000),
    ("Eve", 29, "HR", 65000),
    ("Frank", 38, "Finance", 80000),
    ("Grace", 31, "IT", 78000),
]
# Tasks:
# Filter employees who are older than 30.
# Map the filtered employees to a tuple of (Name, Department, Salary).
# Use reduce to find the total salary of employees in the filtered list.

# Create a list of departments of these filtered employees using map and then use set to get unique departments.
# Sort the filtered employees by salary in descending order.
# Use enumerate and zip to create a numbered list pairing employee names and their departments after sorting.

# Your goal:
# Write a clean Python script using these functions and one-liners where possible to output:
# Total salary of employees older than 30
# Unique departments of these employees
# A numbered, sorted list of employee names and their departments by salary


# Step 1: Filter employees > 30
older_30 = list(filter(lambda emp: emp[1] > 30, employees))

# Step 2: Map to (Name, Department, Salary)
mapped = list(map(lambda emp: (emp[0], emp[2], emp[3]), older_30))

# Step 3: Total salary via reduce
total_salary = reduce(lambda acc, sal: acc + sal, map(lambda emp: emp[3], older_30))

# Step 4: Unique departments
unique_departments = set(emp[2] for emp in older_30)

# Step 5: Sorted by salary descending
sorted_emps = sorted(mapped, key=lambda emp: emp[2], reverse=True)

# Output
print(f"Total Salary of Employees > 30: ₹{total_salary}")
print(f"Unique Departments: {', '.join(unique_departments)}")
print("\nRanked Employee List:")
print("No | Name     | Department | Salary")
print("------------------------------------")
for i, (name, dept, sal) in enumerate(sorted_emps, start=1):
    print(f"{i:<2} | {name:<8} | {dept:<10} | ₹{sal}")
