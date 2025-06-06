d = {} #Empty Dictionary
dict = {
    "Rahul" : 100,
    "Tarak" : 98,
    "Dev" : [101, 25, 95] # List as a value of particular Key
}

print(dict["Dev"]) #Prints the value corresponding to that particular key
print(dict)

#We cannot access key value pairs of a dict using indices eg. dict[0]
#Dictionary is also called as list of key value pairs
#Dict is Mutable as list
#Dict is indexed it means if i want corresponding value for a key it doesn't have
#to check all keys for mapping

print(dict.items()) 
# print(dict.keys())
# print(dict.values())
# dict.update({"Rahul" : 90, "Chaman" : 150 })
# print(dict)

print(dict["Dev"]) 
print(dict.get("Dev"))

dict.pop("Dev") #Remove Corresponding key value pair
print(dict)
