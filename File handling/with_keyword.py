with open("intro.txt") as file:
    print(file.read())

# this code works as exactly as below
# file = open("intro.txt")
# print(file.read())
# file.close()

# so in the with statement we don't have to close file manually.....