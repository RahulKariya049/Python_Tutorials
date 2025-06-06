def Sum_(*args):
    print("This Function gets arguements in form of tuple")
    print(type(args))
    print(f"Tuple recieved: {args}")
    #We can also print tuple by for loop
    for arguements in args:
        print(arguements, end=" ")
    return sum(args)

print(f"\n{Sum_(1, 2, 5)}")
# print(Sum_(1, 5, 78, 90))