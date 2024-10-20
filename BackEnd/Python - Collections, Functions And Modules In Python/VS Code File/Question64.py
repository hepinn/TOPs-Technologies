'''Write a Python program to find the maximum and minimum numbers
from the specified decimal numbers.'''

num1 = float(input("Enter the first decimal number: "))
num2 = float(input("Enter the second decimal number: "))
num3 = float(input("Enter the third decimal number: "))

max_num = num1
min_num = num1

if num2 > max_num:
    max_num = num2
if num2 < min_num:
    min_num = num2

if num3 > max_num:
    max_num = num3
if num3 < min_num:
    min_num = num3

print("Maximum number: ", max_num)
print("Minimum number: ", min_num)