from bitarray import bitarray
from io import StringIO
zero = '0'

File = open('testoutput.txt', 'rb').read()
print(File)
print(bin(File[0]))
print(zero * (8 - len(bin(File[1])[2:])) + bin(File[1])[2:])

#print("byte 0",File[0])

import ast, json

with open('dict.json', 'r') as f: 
    data = f.read()

originalDictionary = json.loads(data)

#find short and long character lengths:
holder = 0
happened = False
lShortChar = 0
lLongChar = 0
for item in originalDictionary:
    length = len(originalDictionary[item])
    if length > holder:
        holder = length
        if happened:
            lLongChar = length
        else:
            lShortChar = length
        happened = True


#reverse dictionary:
Dictionary = dict(map(reversed, originalDictionary.items()))


for index in Dictionary:
    print(index,Dictionary[index])

def access_bit(data, num):
    base = int(num // 8)
    shift = int(num % 8)
    return (data[base] & (1<<shift)) >> shift



zero = '0'
fileBinaryString = ''
leftPointer = 0
rightPointer = 1
bytesList = bytearray(File)
import os
for index in range(os.stat('testoutput.txt').st_size):
    fileBinaryString = fileBinaryString + zero * (8 - len(bin(File[index])[2:])) + bin(File[index])[2:]                         #fileBinaryString
print(fileBinaryString)



def decompress(fS,dict):
    leftPointer = 0
    rightPointer = 0
    outputString = ''
    
   # if rightPointer >= len(fS) or leftPointer >= len(fS):
  #      break

    while 1:

        if leftPointer + lShortChar > len(fS):
            break

        if fS[leftPointer] == '0':
            rightPointer = leftPointer + lShortChar
            outputString = outputString + dict[fS[leftPointer:rightPointer]]
            leftPointer = rightPointer

        if fS[leftPointer] == '1':
            rightPointer = leftPointer + lLongChar
            outputString = outputString + dict[fS[leftPointer:rightPointer]]
            leftPointer = rightPointer


    return outputString

print(decompress(fileBinaryString,Dictionary))

decompOutput = open('poopdecomp.txt','w')
decompOutput.write(decompress(fileBinaryString,Dictionary))

