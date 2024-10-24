# Q.6 Write a Python program to read a file line by line and store it into a list.

L = ["xyz\n", "for\n", "xyz\n"]

file1 = open('xyz.txt', 'w')
file1.writelines(L)
file1.close()

file1 = open('xyz.txt', 'r')
Lines = file1.readlines()

count = 0
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
