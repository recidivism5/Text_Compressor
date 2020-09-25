from bitarray import bitarray
from io import StringIO

File = open('output.txt', 'rb').read()
#print(File)

#print("byte 0",File[0])

import ast, json

with open('dict.json', 'r') as f: 
    data = f.read()

originalDictionary = json.loads(data)
Dictionary = dict(map(reversed, originalDictionary.items()))

for index in Dictionary:
    print(index,Dictionary[index])

def access_bit(data, num):
    base = int(num // 8)
    shift = int(num % 8)
    return (data[base] & (1<<shift)) >> shift


#print(access_bit(File,-21))

#for byte in wholeFileString

fileBinaryString = ''
#print("byte 1",File[1])
#print(bin(File[1])[2:])
leftPointer = 0
rightPointer = 1
bytesList = bytearray(File)
for index in File:
    fileBinaryString = fileBinaryString + bin(File[index])[2:]
#print(fileBinaryString)
