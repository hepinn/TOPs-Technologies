# Q.8 Write  Python to test whether a passed letter iss a vowel or not.


character=input("Enter Any Character :")
# list of vowels

vowels=['a','e','i','o','u','A','E','I','O','U']

if character in vowels:
    print(character,"is a vowel")
else:
    print(character,"is consonant")
    
