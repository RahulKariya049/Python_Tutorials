# Challenge: Vector2D Class — Operator Overloading & Custom Behavior
# You're going to build a simple 2D vector class (like in physics) and add Pythonic behavior using dunder methods.

# 🎯 Your Goals:
# Implement a class Vector2D with the following functionality:

# 🔹 Basic Setup
# __init__(self, x, y) — store x and y coordinates.
# __repr__ — show a useful developer string.
# __str__ — user-friendly output like "Vector(3, 4)".

# 🔹 Operator Overloading
# __add__ — add two vectors (v1 + v2)
# __sub__ — subtract vectors
# __mul__ — scalar multiplication (v * 3)
# __eq__ — equality comparison (v1 == v2)
# __abs__ — magnitude of vector using abs(v) (hint: use math.hypot)

# 🔹 Extra (Optional but Powerful)
# __len__ — returns 2 (dimensionality of vector)
# __getitem__ — allow v[0] to give x, v[1] to give y
# __iter__ — make the vector iterable (for i in v:)

import math
class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
    
    def __str__(self):
        return f"{self.x}i + {self.y}j"
    
    def __add__(self, vec):
        return Vector(self.x + vec.x, self.y + vec.y)
    
    def __sub__(self, vec):
        return Vector(self.x - vec.x, self.y - vec.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, vec):
        return ((self.x == vec.x) and (self.y == vec.y))
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __len__(self):
        return 2
    

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)              # "Vector(3, 4)"
print(repr(v1))        # "Vector2D(x=3, y=4)"

print(v1 + v2)         # Vector(4, 6)
print(v1 - v2)         # Vector(2, 2)
print(v1 * 3)          # Vector(9, 12)

print(v1 == v2)        # False
print(abs(v1))         # 5.0

print(len(v1))         # 2
# print(v1[0], v1[1])    # 3 4

# for val in v1:
#     print(val)         # 3 \n 4
