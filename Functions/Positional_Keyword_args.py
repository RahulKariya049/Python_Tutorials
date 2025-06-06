#POSITIONAL ARGUEMENTS
def greet(name):
    print(f"Hello {name}")

greet("Alice")  # Positional
greet(name="Alice")  # Also allowed unless restricted

#KEYWORD ARGUEMENTS
def greet(name="Guest", age=0):
    print(name, age)

greet(age=21, name="Bob")  # OK — keyword style


# / = Positional-only separator
# All arguments before / must be positional.

def f(a, b, /):
    print(a, b)

f(1, 2)             # OK
# f(a=1, b=2)       Error: keyword not allowed

# * = Keyword-only separator
# All arguments after * must be keyword.

def f(*, a, b):
    print(a, b)

# f(1, 2)           ❌ Error: must use keywords
f(a=1, b=2)         # ✅ OK
