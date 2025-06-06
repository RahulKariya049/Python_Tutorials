names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

zipped = zip(names, scores)
print(list(zipped))  # [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
# If the lists are unequal in length, zip() stops at the shortest one.

for i, name in enumerate(names):
    print(f"{i} → {name}")
# What it does:
# Adds a counter to an iterable, so you get (index, value) while looping.