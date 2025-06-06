#Basic Function syntax
#write function to find square of a number.

def square_num(num):
    return num ** 2

print(f"Square Function:(4) {square_num(4)}")

#Function with multiple Parameters

def sum(num1, num2):
    return num1 + num2

print(f"Sum Function:(2, 9) {sum(2, 9)}")


def multiply(p1 , p2):
    return p1 * p2

print(f"Multiply integers:(2, 9) {multiply(2, 9)}")
print(f"Multiply Strings:(2, 9) {multiply(2, 'Ra')}")
# print(f"Multiply Strings:(2, 9) {multiply('t', 'Ra')}") gives ERROR


#Multiple return values
import math
def circle(radius):
    return math.pi * (radius ** 2) , 2 * math.pi * radius

a, c = circle(4)
print(f"Area, Circumference of circle with raius 4: {round(a, 2)} {round(c, 2)}")
