import numpy
import io

Dictionary = {

}

f = open("poop.txt","r")

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

print(DtB(5))
  

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




#stolen stackoverflow code:
from io import StringIO
def write_bitstream(fname, bits):
    # bits are a string of ones and zeros, based on this
    # stackoverflow answer: https://stackoverflow.com/a/16888829/6938913
    # was broken due to utf-8 encoding using up to 4 bytes: https://stackoverflow.com/a/33349765/6937913
    sio = StringIO(bits)
    with open(fname, 'wb') as f:
        while 1:
            # Grab the next 8 bits
            b = sio.read(8)
            # Bail if we hit EOF
            if not b:
                break
            # If we got fewer than 8 bits, pad with zeroes on the right
            if len(b) < 8:
                b = b + '0' * (8 - len(b))
            # Convert to int
            i = int(b, 2)
            # Write
            f.write(i.to_bytes(1, byteorder='big'))

wholeFileString = open('poop.txt', 'r').readlines()
oString = ''
for line in wholeFileString:
    for character in line:
        oString = oString + Dictionary[character]
print(oString)
write_bitstream('output.txt',oString)









'''    00001100001

    bytesList = []
    outputByteArray = bytearray(bytesList)
    outputFile = open("output.txt","wb")
    outputFile.write(outputByteArray)

    Dicionary[frequencyArray[index]] = bytearray()'''

#for line in f:
 #   for character in line:

# Pass "wb" to write a new file, or "ab" to append
#with open("output.txt", "wb") as binary_file:
    # Write text or bytes to the file
 #   binary_file.write("Write text by encoding\n".encode('utf8'))
  #  binary_file.write("cringe.jpg\n".encode('ascii'))
   # num_bytes_written = binary_file.write(b'\xDE\xAD\xBE\xEF\x74\x74\x74\x74')
    #print("Wrote %d bytes." % num_bytes_written)


#longCharBitLength = 

#for line in f:
 #   for character in line:
