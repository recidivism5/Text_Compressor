import numpy
import io

Dictionary = {

}

f = open("poop.txt","r")

for line in f:
    for c in line:
        print(c)
        if c in Dictionary:
            Dictionary[c] += 1
        else:
            Dictionary[c] = 1

q = 0
indexHolder = ""
frequencyArray = []
while Dictionary:
    q = 0
    for index in Dictionary:
        print(index,Dictionary[index])
        if Dictionary[index] > q:
            q = Dictionary[index]
            indexHolder = index
    frequencyArray.append(indexHolder)
    del Dictionary[indexHolder]
    print("index",index)
    print("indexHolder",indexHolder)

print("characters in order of frequency:")
for element in range(len(frequencyArray)):
    print(frequencyArray[element])

requiredCharacters = len(frequencyArray)
print(requiredCharacters)

def gp2(target):
    i = 0
    while i > -1:
        if pow(2,i) > target:
            break
        else:
            i += 1
    return i

longCharBitLength = gp2(requiredCharacters) + 1
requiredCharacters -= pow(2,gp2(requiredCharacters))
shortCharBitLength = gp2(requiredCharacters) + 1




#longCharBitLength = 

#for line in f:
 #   for character in line:
