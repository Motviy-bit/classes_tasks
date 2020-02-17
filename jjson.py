import json
with open('jjson.json','r') as f:
    data = json.load(f)
b = 0
m = 0
names30_ = []
for item in data:
    x = item.get('eyeColor')
    if x == 'blue':
        print(item.get('name'))
    y = item.get('gender')
    if y == 'male':
        m += 1
    else:
        b += 1
print(f'Количество людей женского пола: {b}. Количество людей мужского пола: {m}')
    age_ = item.get('age')
    if age_ > 30:
        names30_.append(item)

with open('names30.json','w') as f:
    json.dump(names30_,f, ensure_ascii=False, indent=4)




