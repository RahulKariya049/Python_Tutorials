def outer(msg):
    def inner():
        print(f"Message was: {msg}")
    return inner

printer = outer("Hello world")
printer()
# Let’s pause at each step to understand why.

# 🧠 Step-by-step What’s Happening
# 🔹 Step 1: Define outer
# Nothing runs yet.
# Just stores the blueprint of outer in memory.

# 🔹 Step 2: Call outer("Hello world")
# A new variable msg = "Hello world" is created inside outer’s local scope.
# Python defines the inner() function — but does NOT call it yet.
# inner() now remembers msg from the outer environment.
# The outer() function returns the inner() function object.
# So now:

printer = outer("Hello world")
# Means:
# You stored inner() into the name printer
# And printer() has access to msg = "Hello world" even though outer() has finished

# 🔹 Step 3: Now you call printer()
# You’re calling the function inner() that was returned earlier.
# When it runs, it prints the remembered message "Hello world" — from outer’s environment.

# This is why inner can use msg even though msg was not defined inside it directly.
# It's using a variable captured from the outer scope — that’s the closure.

#Similar Example
def make_power(exp):
    def value(base):
        return base ** exp
    return value

square = make_power(2)
cube = make_power(3)

print(square(3))
print(cube(8))


#  Challenge 2: Prefix Logger
# 🧠 Goal: Write a closure make_logger(prefix) that returns a function which logs messages with that prefix.
# info = make_logger("INFO")
# warn = make_logger("WARNING")

# info("User logged in")     # Output: [INFO] User logged in
# warn("Low battery")        # Output: [WARNING] Low battery

def make_logger(prefix):
    def inner(message):
        print(f"[{prefix}] {message}")
    return inner

info = make_logger("INFO")
warn = make_logger("WARNING")

info("User logged in")     # Output: [INFO] User logged in
warn("Low battery")        # Output: [WARNING] Low battery


# ⚔️ Challenge 3: Custom Filter Generator
# 🧠 Goal: Write filter_longer_than(n) that returns a function to filter words longer than n.

# Then use it with filter().

def filter_longer_than(n):
    def inner(l):
        return list(filter(lambda x : len(x)>n, l))
    return inner

longer_than_4 = filter_longer_than(4)
words = ["apple", "is", "banana", "go", "elephant"]
print(longer_than_4(words))