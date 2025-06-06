list1 = [] # Empty List
print(type(list1))

# List can accomodate any data type and lists are mutable
# it means when we apply any methods on list it does not
# return whole list it changes the original list
list2 = ["Rahul", 34, 3.321, True, "Hello"]

# We can access list items through index
print(list2[0])
list2.append(1) # append function 
list2.append(2)
print(list2[5] + list2[6])

l3 = [1, 65, 30, 48, 78, 100, 78]
print(l3.count(78)) # Count function returns the occurrence of a specific element
l3.sort()
print(l3)
l3.reverse()
print(l3)
l3.remove(65)
print(l3)
l3.pop(2) # it is same as remove function but takes index as an argument
print(l3)
print(sum(l3)) #Returns the sum of all elements of tuple
print(len(l3))
print(max(l3), min(l3))

l4 = []
# append function appends as a string if we don't
# use int() fun because by default input takes as string
l4.append(int(input("Enter a  valid Number:\n")))
l4.append(int(input("Enter another Number:\n")))

print(l4[0] + l4[1])
