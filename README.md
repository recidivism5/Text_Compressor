# Text_Compressor
Compresses text

compressor.py compresses a text file using a frequency dictionary unique to that file. The dictionary elements are placed at the beginning of the compressed file. 

decompressor.py unpacks the dictionary at the beginning of a compressed file and uses it to decompress the rest of the file.

Usage:

>python compressor.py [target file name] [output file name]        #Outputs a compressed version of the target file

>python decompressor.py [target file name] [output file name]      #Outputs a decompressed version of the target file


Bracketed arguments can be location pointers, so you can do this, for example:

python compressor.py C:\Users\ian\Documents\funnyDocument.txt C:\Users\ian\Documents\funnyDocumentCompressed.txt


To compress a file and output the dictionary used to compress that file, give the name of the file you want to contain that dictionary as a third argument in command prompt:

>python compressor.py [target file name] [output file name] [dictionary file name]
