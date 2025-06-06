#Challenge 1
# ✅ Write a one-liner using filter and map to:
# → filter even numbers
# → square them

# Your code here 👇

nums = [x for x in range(1,11)]
even_nums_square = list(filter(lambda x: x % 2 == 0 , map(lambda x: x**2 , nums)))
print(even_nums_square)


#Challenge 2
# ✅ Use filter to extract only strings,
# then use map to make them uppercase.

# Your code here 👇

items = ["hello", 123, "world", 45.6, "python"]
str_items = list(map(lambda x : x.upper(), filter(lambda x : type(x) == str , items)))
print(str_items)


from functools import reduce

nums = [1, 2, 3, 4]

# ✅ Use map to cube the numbers, then reduce to sum them
# Final result should be: 1³ + 2³ + 3³ + 4³ = 100
# This effectively reduces the iterable to a single value. If initial is present,
# it is placed before the items of the iterable in the calculation, and serves as
# a default when the iterable is empty.

# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
# calculates ((((1 + 2) + 3) + 4) + 5).
# Your code here 👇
var = reduce(lambda x,y : x + y, list(map(lambda x : x**3 , nums)))
print(var)



# Challenge 4
# You’re given a list of strings.
# Sort them in descending order based on the number of vowels in each string.
#  How sorted() Works With key=
# sorted(iterable, key=some_function, reverse=False)
# key= tells Python:
# ➤ “When comparing two items, compare based on the value returned by this function.”

# So even if you're sorting strings, the comparison can be done based on any metric, like vowel count, length, ASCII sum, etc.


words = ["banana", "apple", "grape", "kiwi", "orange", "blueberry"]

sorted_words = sorted(words, key=lambda word: sum(1 for ch in word.lower() if ch in "aeiou"), reverse=True)
print(sorted_words)


#  Challenge: Sort Students by Average Marks
# You're given a list of student records in the format:
# ✅ Goal:
# Sort this list in descending order based on each student's average score.

from statistics import mean

students = [
    ("Alice", [85, 92, 78]),
    ("Bob", [70, 88, 90]),
    ("Charlie", [95, 100, 92]),
    ("Daisy", [60, 65, 70]),
]

avg_sort_list = sorted(students , key= lambda tuple: mean(tuple[1]), reverse=True)
print(avg_sort_list)