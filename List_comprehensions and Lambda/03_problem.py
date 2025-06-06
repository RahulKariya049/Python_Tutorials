# Now let’s use that knowledge with zip() and enumerate() to solve the earlier ranking problem:

# Problem Recap:

students = ['Alice', 'Bob', 'Charlie', 'Daisy']
marks = [91, 85, 77, 92]
# Goal: Print a ranked list from highest to lowest mark, like:

# 1. Daisy - 92
# 2. Alice - 91
# 3. Bob - 85
# 4. Charlie - 77
# Step 1: Zip name with score
paired = zip(students, marks)

# Step 2: Sort based on marks (descending)
sorted_list = sorted(paired, key=lambda x: x[1], reverse=True)

# Step 3: Print with rank
for rank, (name, score) in enumerate(sorted_list, start=1):
    print(f"{rank}. {name} - {score}")