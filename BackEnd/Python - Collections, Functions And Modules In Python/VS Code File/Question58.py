#Write a Python program to read a random line from a file.

import random

file_path = 'Tops1.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

if lines:
    random_line = random.choice(lines)
    print(random_line.strip())
else:
    print("The file is empty.")