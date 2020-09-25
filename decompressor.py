from io import StringIO

wholeFileString = open('output.txt', 'rb').read()
print(wholeFileString)

import ast, json

with open('dict.json', 'r') as f: 
    data = f.read()

originalDictionary = json.loads(data)
Dictionary = dict(map(reversed, originalDictionary.items()))

for index in Dictionary:
    print(index,Dictionary[index])

#for byte in wholeFileString

