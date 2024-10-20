# Q.9 Write a python function that takes two lists and return true if they have at least one common member.

def cdata(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result 
    return result
    

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(cdata(a, b))
 
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(cdata(a, b))