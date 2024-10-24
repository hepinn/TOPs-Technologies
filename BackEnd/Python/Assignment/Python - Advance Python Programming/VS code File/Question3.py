# Q.3 Write a Python program to append text to a file and display the text. 


def file_read(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
                myfile.write("Python is Good Language\n")
                myfile.write("Python is very Good Language")
        txt = open(fname)
        print(txt.read())
file_read('abc.txt')
