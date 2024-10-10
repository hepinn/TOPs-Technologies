# Q.10 Write a Python program that will return true if two given integer values are equal or their sum or difference is 5.


x=int(input("Enter a 1st value :"))
y=int(input("Enter 2nd value :"))
if x==y or x-y==5 or x+y==5:
    print(True)
else:
    print(False)
