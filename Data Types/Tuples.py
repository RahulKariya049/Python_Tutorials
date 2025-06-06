t1 = () # Empty 
t2 = (1,) # Tuple with only one element if you don't write , python will take as int
print(type(t1))

# Tuples are similar as Lists but the differnce between them is
# Tuple is immutable as Strings

t3 = ("Apple", "Orange", 34, 0.292, True)

# we can access its element through index also
print(t3[0])

t4 = (1, 68, 69, 87, 65, 1)
print(t4.count(1)) #Returns the number of occurrences of a specified value in the tuple.
print(t4.index(69)) #Returns index of it's First occurrence
print(sum(t4)) #Returns the sum of all elements of tuple
print(len(t4))
print(max(t4), min(t4))