from io import StringIO

wholeFileString = open('output.txt', 'rb').read()
print(wholeFileString)

import ast, json

with open('dict.json', 'r') as f: 
    data = f.read()

Dictionary = json.loads(data)

for index in Dictionary:
    print(index,Dictionary[index])

