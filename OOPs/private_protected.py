class Dog:
    def __init__(self):
        self._mood = "happy"

d = Dog()
print(d._mood)  # ✅ Works — not protected by Python!


class Cat:
    def __init__(self):
        self.__secret = "I eat your snacks"

c = Cat()
# print(c.__secret)       ❌ AttributeError!
print(c._Cat__secret)     # ✅ Works via name mangling


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

c = Circle(10)
print(c.radius)   # ✅ No () needed — it's like a variable!

# You defined radius as a property with only a getter.
# Since there's no setter defined, Python assumes you want radius to be read-only.

