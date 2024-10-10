# Q.23 Write a Python function to insert a string in the middle of a string. 

def insert_string_middle(str, word):
    return str[:2] + word + str[2:]

print(insert_string_middle('[[]]', 'Hepin'))  
print(insert_string_middle('{{}}', 'Druv'))    
print(insert_string_middle('<<>>', 'Raj'))   

