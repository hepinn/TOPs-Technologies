#Write a Python program to remove an empty tuple(s) from a list of tuples.

tuples_list = [(), ('a', 'b'), (), ('c', 'd'), (), ('e', 'f'), ()]
tuples_list = [t for t in tuples_list if t]
print(tuples_list)