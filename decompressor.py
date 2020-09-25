
import ast, json

with open('dict.json', 'r') as f: 
    data = f.read()

Dictionary = json.loads(data)

for index in Dictionary:
    print(index,Dictionary[index])

