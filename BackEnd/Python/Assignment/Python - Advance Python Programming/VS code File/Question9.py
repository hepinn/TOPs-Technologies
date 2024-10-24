# Q.9 Write a Python program to count the number of lines in a text file. 

with open(r"xyz.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)