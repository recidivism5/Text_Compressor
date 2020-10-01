import numpy
import io
import sys

argsList = sys.argv         # sys.argv[1] is target compressed file. sys.argv[2] is compressed output file.

Dictionary = {

}

f = open(sys.argv[1],errors='ignore')

for line in f:
    for c in line:
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

hex(int('010110', 2))

longCharBitLength = gp2(requiredCharacters)
print("longCharBitLength:",longCharBitLength)
requiredCharacters -= pow(2,longCharBitLength-1)
print(requiredCharacters)
shortCharBitLength = gp2(requiredCharacters) + 1
print("shortCharBitLength:",shortCharBitLength)
longCharPossibleValues = pow(2,longCharBitLength-1)
shortCharPossibleValues = pow(2,shortCharBitLength-1)

print((pow(2,longCharBitLength-1),pow(2,shortCharBitLength-1)))


#build compression dictionary:
Dictionary = {}
binaryContainer = f.read()
zero = '0'
one = '1'

def DtB(n):  
    return bin(n).replace("0b", "")
  

#Build compression dictionary:
for index in range(len(frequencyArray)):

    if index < shortCharPossibleValues:
        lz = zero * (shortCharBitLength - len(DtB(index)))
        Dictionary[frequencyArray[index]] = lz + DtB(index)
    else:
        lz = one + (zero * (longCharBitLength - (len(DtB(index-shortCharPossibleValues)) + 1)))
        Dictionary[frequencyArray[index]] = lz + DtB(index-shortCharPossibleValues)


for item in Dictionary:
    print(item,Dictionary[item])


#Put the whole file into a readlines() array of strings, iterate through the characters of it and run it through the compression dictionary.
#Write the resulting binary to an output file.
oString = ''
wholeFileString = open(sys.argv[1], errors='ignore').readlines()
for line in wholeFileString:
    for character in line:
        oString = oString + Dictionary[character]
#print(oString)
oString = oString + (zero * (8 - (len(oString) % 8)))                   #extra compression % if turned off ???
print("len(oString): ",len(oString))
#print(oString)

with open(sys.argv[2],'wt') as f:
    for element in range(len(frequencyArray)):
        f.write(frequencyArray[element])
    f.write('§')

with open(sys.argv[2],'ab') as f:
    f.write(bytes(int(oString[i : i + 8], 2) for i in range(0, len(oString), 8)))

