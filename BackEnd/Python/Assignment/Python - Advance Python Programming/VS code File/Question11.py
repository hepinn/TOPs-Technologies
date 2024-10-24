# Q.11 Write a Python program to write a list to a file. 

l = ['Tops','for','Tops!']
with open('Tops1.txt', 'w+') as f:
    for items in l:
        f.write('%s\n' %items)
    
    print("File written successfully")
f.close()    
