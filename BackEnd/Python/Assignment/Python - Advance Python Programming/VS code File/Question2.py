# Q.2 Write a python program to read an entire text file.


def file_read(fname):
        txt = open(fname)
        print(txt.read())

file_read('Tops.txt')
