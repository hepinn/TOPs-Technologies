#Write a Python program to check multiple keys exists in a dictionary

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

keys_to_check = ['a', 'c', 'e']

for key in keys_to_check:
    if key in my_dict:
        print("Key",key,"exists in the dictionary.")
    else:
        print("Key",key,"does not exist in the dictionary.")