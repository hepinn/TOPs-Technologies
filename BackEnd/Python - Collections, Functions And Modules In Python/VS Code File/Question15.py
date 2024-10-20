# Write a Python program to get unique values from a list

mlist = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original List : ", mlist)
my_set = set(mlist)
newlist = list(my_set)

print("List of unique numbers : ", newlist)