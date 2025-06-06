# return	                                yield
# Exits the function completely	        Pauses the function, saves state
# Returns a single value	                Can produce multiple values (lazy)
# Can’t resume	                        Resumes from where it left off

def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i

# let's say we are expecting things like:
# we will call function even_generator in loop and it should return even number everytime we call
# in order like first call: 2 other: 4, 6, 8 and so on...
# but the problem is we will call function every time so if we use return it will give the same 
# output so yeild is use to also save the last function call

for num in even_generator(100000):
    print(num, end = " ")