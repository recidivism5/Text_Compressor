from bitarray import bitarray
from io import StringIO
import sys
zero = '0'
one = '1'

argsList = sys.argv         # sys.argv[1] is the target compressed file

#build frequencyArray from start of compressed file and set position to the starting bit index of the compressed portion of the file data:
frequencyArray = []
position = 1
with open('testoutput.txt',errors='ignore') as f:
    while 1:
        container = f.read(1)
        position += 1
        if container == '§':
            break
        frequencyArray.append(container)
position = (position * 8)


#Determine long and short bitlengths:
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

longCharBitLength = gp2(requiredCharacters)
print("longCharBitLength: ",longCharBitLength)
requiredCharacters -= pow(2,longCharBitLength-1)
print(requiredCharacters)
shortCharBitLength = gp2(requiredCharacters) + 1
print("shortCharBitLength: ",shortCharBitLength)
longCharPossibleValues = pow(2,longCharBitLength-1)
shortCharPossibleValues = pow(2,shortCharBitLength-1)

print((pow(2,longCharBitLength-1),pow(2,shortCharBitLength-1)))

#Build decompression dictionary:
def DtB(n):                                                     #Decimal to binary
    return bin(n).replace("0b", "")

Dictionary = {}
for index in range(len(frequencyArray)):

    if index < shortCharPossibleValues:
        lz = zero * (shortCharBitLength - len(DtB(index)))
        Dictionary[frequencyArray[index]] = lz + DtB(index)
    else:
        lz = one + (zero * (longCharBitLength - (len(DtB(index-shortCharPossibleValues)) + 1)))
        Dictionary[frequencyArray[index]] = lz + DtB(index-shortCharPossibleValues)
#Reverse dictionary
Dictionary = dict(map(reversed, Dictionary.items()))
for item in Dictionary:
    print(item,Dictionary[item])




#Open file in read byte mode:
File = open('testoutput.txt', 'rb').read()
fileBinaryString = ''

#Fill fileBinaryString with file data:
import os
for index in range(os.stat('testoutput.txt').st_size):
    fileBinaryString = fileBinaryString + zero * (8 - len(bin(File[index])[2:])) + bin(File[index])[2:]                         #fileBinaryString
print(fileBinaryString)



def decompress(fS,dict):
    leftPointer = position
    rightPointer = 0
    outputString = ''
    
   # if rightPointer >= len(fS) or leftPointer >= len(fS):
  #      break

    while 1:

        if leftPointer + shortCharBitLength > len(fS):
            break

        if fS[leftPointer] == '0':
            rightPointer = leftPointer + shortCharBitLength
            outputString = outputString + dict[fS[leftPointer:rightPointer]]
            leftPointer = rightPointer

        if fS[leftPointer] == '1':
            rightPointer = leftPointer + longCharBitLength
            outputString = outputString + dict[fS[leftPointer:rightPointer]]
            leftPointer = rightPointer


    return outputString

print(decompress(fileBinaryString,Dictionary))

decompOutput = open('poopdecomp.txt','w')
decompOutput.write(decompress(fileBinaryString,Dictionary))