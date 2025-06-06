def keyword_args(**kwargs):
    print("We get a dict as arguement which have key as parameter name and value as parameter")
    print(type(kwargs))
    print(f"Dictionary we got is: {kwargs}")

    #we can print using for loop also
    for key,value in kwargs.items():
        print(f"{key} : {value}")

keyword_args(name="Superman", power="Chori-Chakkari", baap="Kala-naag", size="Butka")