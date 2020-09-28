# Text_Compressor
Compresses text

compressor.py compresses a text file using a frequency dictionary unique to that file. The dictionary elements are placed at the beginning of the compressed file. 

decompressor.py unpacks the dictionary at the beginning of a compressed file and uses it to decompress the rest of the file.

Usage:

>python compressor.py [target file name] [output file name]        #Outputs a compressed version of the target file

>python decompressor.py [target file name] [output file name]      #Outputs a decompressed version of the target file
