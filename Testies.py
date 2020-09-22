import numpy

Dictionary = {

}

f = open("test.txt","r")

for line in f:
    for c in line:
        print(c)
        if c in Dictionary:
            Dictionary[c] += 1
        else:
            Dictionary[c] = 1

for index in Dictionary:
    print(index,Dictionary[index])