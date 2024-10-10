# Write a Python program to count the number of characters (character
# frequency) in a string

chr=input("Enter a Words :")
freq={}

for i in chr:
    if i in freq:
        freq[i]+=1
        print(freq)
    else:
        freq[i]=1
        print(freq)
        