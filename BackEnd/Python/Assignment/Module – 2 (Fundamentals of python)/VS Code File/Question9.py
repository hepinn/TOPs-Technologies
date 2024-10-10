# Q.9 Write a python program to sum of three given integers, However, if two values are equal sum will be zero.

x=int(input("Enter 1st Value :"))
y=int(input("Enter 2nd Value :"))
z=int(input("Enter 3rd Value :"))
if x==y or y==z or x==z:
    sum=0
    print(sum)
else:
    sum=x+y+z
    print(sum)
    
    
    