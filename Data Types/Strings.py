# String Declaration
a = "Str1"
b = 'Str2'
c = '''Multi Line Strings we can enter within triple single quotes'''

# String Slicing
# Note: String is immutable
name = "Rahul"
# 0:3 means start with index 0 till index 3 without including index 3
substr = name[0:3]
substr1 = name[1:4]
substr2 = name[2:3]

print(f"Sliced Strings: {substr}, {substr1}, {substr2}")

# negative indicing
# Rahul
# 01234
# -5-4-3-2-1
substr = name[-5:-2] #[0:3]
substr1 = name[-4:-1] #[1:4]
substr2 = name[-3:3] #[2:3]

print(f"Negatively Sliced Strings: {substr}, {substr1}, {substr2}")

str = "0123456789"
print(f"Advanced Slicing: {str[1:9:3]}")  #in substr 1:9 start with index 1 and skip next 2 index

# String Functions
stran = "rahullalul"

print(len(stran))
print(stran.endswith("ul")) #similarly startswith Function
print(stran.capitalize()) #Capitalize the first letter
print(stran.count("l")) #occurence of a character 

st = "Hello Rahul"
print(st.replace("Rahul", "World"))
print(st.find("Rahul")) # returns the index where it finds it otherwise  returns -1
print(st.find("B"))

chai = "  Masala Chai  " #Extra Spaces 
print(f"Stripped string: {chai.strip()} Original String: {chai}")

chai = "Lemon, Masala, Ginger, Mint"
list = chai.split(", ")
print(list)

#joining elements of list into string
str = "-".join(list)
print(str)