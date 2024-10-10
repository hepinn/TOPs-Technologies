# Write a python program to get the fibonacci series of given range.

n=int(input("Enter the range of fibonacci : "))
a,b=0,1
print(a,end=" ")
while b<n:
    print(b,end=" ")
    a,b=b,a+b