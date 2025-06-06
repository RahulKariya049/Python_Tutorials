# 🔹 What Are Dunder Methods in Python?
# Dunder stands for "Double UNDERscore", and these methods are also known as magic methods or special methods.

# They are named with double underscores before and after the method name, like:

# __init__, __str__, __len__, __add__, __getitem__, __call__, ...
# They are not meant to be called directly by you in most cases. Instead, Python calls them automatically in certain situations to provide special behavior for your objects.

# Python automatically uses them when specific syntax is encountered:

# Dunder Method	                                    Triggered By
# __init__	                                        Object creation
# __str__	                                            print(obj) or str(obj)
# __len__	                                            len(obj)
# __getitem__	                                        obj[key]
# __iter__, __next__	                                for item in obj
# __eq__	                                            obj1 == obj2
# __add__	                                            obj1 + obj2