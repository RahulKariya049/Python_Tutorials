def decorator_function(func):
    def wrapper():
        print("Something before the function runs")
        func()
        print("Something after the function runs")
    return wrapper

@decorator_function
def say_hello():
    print("Hello!")

say_hello()

# this line: @decorator_function is syntactics sugar for:
#            say_hello = decorator_function(say_hello)

#in this example decorator function will do one thing is return the original function but 
#with wrapper and wrapper has some additional functionalities than original function so 
#now say_hello is updated with that wrapper function and whenever we call org. function
#it does some additional functionalities also 


from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
#add = logger(add)
def add(x, y):
    return x + y

result = add(a=3, b=4)
print("Result:", result)

#  So @wraps(func):
# Copies the original function’s metadata (like __name__, __doc__, etc.)
# Helps tools like IDEs, debuggers, and documentation generators
# Avoids confusion in debugging and tracing

# 🚨 Problem Without @wraps

print(add.__name__)      # 😢 Outputs: wrapper
print(add.__doc__)       # 😢 Outputs: None
# 🧠 Why this happens:
# Python now sees greet = wrapper, so when you ask for greet.__name__, it gives "wrapper", not "greet". The __doc__ string is also lost.

