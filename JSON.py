import json
with open('source/person.json','r') as f:
    data = json.load(f)
    print(data)

for item in data:
    print(item.get('eyeColor'))