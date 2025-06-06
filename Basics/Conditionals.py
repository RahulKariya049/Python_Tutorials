#Basic Conditional Program
age = int(input("Enter Your Age: "))

if(age>=18):
    print("You are allowed to vote")

elif(age>18 and age<=21):
    print("You are not allowedd to marry")

elif(age<=0):
    print("Enter Valid age!")

else:
    print("You are not allowed to vote")

#Another Conditional Program which uses in keyword
#Our task is to find out wether the given phrases are present in 
#a string or not

p1 = "Subscribe"
p2 = "Buy Now"
p3 = "Make lot of money"

comment = input("Enter a comment:\n")
if(p1.lower() in comment.lower() or p2.lower() in comment.lower()
    or p3.lower() in comment.lower()):
    print("The Given Comment is Spam!!")