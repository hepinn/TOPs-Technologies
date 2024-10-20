#Write a Python program to check whether an element exists within a tuple.

my_tuple = (1, 2, 3, 4, 5)

element = 3

if element in my_tuple:
    print("The element",element,"exists in the tuple.")
else:
    print("The element",element,"does not exist in the tuple.")