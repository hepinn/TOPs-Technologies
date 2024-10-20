# Q.5 How will you compare two lists?
li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35]

a = []
for element in li1:
    if element not in li2:
        a.append(element)

print(a)