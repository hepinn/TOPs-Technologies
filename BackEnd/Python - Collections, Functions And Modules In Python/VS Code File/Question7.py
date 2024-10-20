# Q.7 Write a python program to remove duplicate from a list.

l = ["a", "b", "a", "c", "c"]
l = list(dict.fromkeys(l))
print(l)