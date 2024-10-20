#Write a Python program to replace last value of tuples in a list.

tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

new_tuples_list = [tuple(list(t)[:-1] + [10]) for t in tuples_list]

print(new_tuples_list)