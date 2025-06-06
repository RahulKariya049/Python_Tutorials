s1 = set() #Empty Set

#Elements in set cannot be repeated 
#order is not mainted in sets
s2 = {5, 9, 32, 56, 5, 5, "Str"} #Strings are also allowed in a set
print(s2, type(s2))
s2.add(59)
s2.remove(56)
print(s2)
s2.clear() #Empties the Set
print(s2)
print(len(s2))

s3 = {12, 30, 25, 1}
s4 = {17, 30, 12, 18, 25, 1}

print(s3.union(s4)) # s3 U s4
print(s3.intersection(s4))# s3 inter s4
print(s3.difference(s4))# s3 - s4
print(s3.issubset(s4))

#Quick Quiz
set = set()
set.add(20)
set.add(20.0)
set.add("20")
#What will be the length of this set? - 3 Wrong!
#Python interpreter considers 20.0 is equal as 20 so length will be 2
print(len(set))