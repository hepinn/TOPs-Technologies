# Write a Python program to get the Factorial number of given number.

num=int(input("Enter a Number : "))
fac=1
if num<0:
    print("Factorial does not exist for negative number")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fac=fac*i
    print("The Factorial of",num,"is",fac)        