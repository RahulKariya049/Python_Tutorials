class NegativeNumberError(Exception):
    pass

def sqrt(x):
    if x < 0:
        raise NegativeNumberError("Cannot take square root of negative number.")
    return x ** 0.5

try:
    result = sqrt(-9)
    print(result)
except NegativeNumberError as e:
    print("Handled:", e)
