import json
with open('jjson.json','r') as f:
    data = json.load(f)
b = 0
m = 0
names30_ = []
for item in data:
# Task № 1
    x = item.get('eyeColor')
    if x == 'blue':
        print(item.get('name'))
# Task № 2
    y = item.get('gender')
    if y == 'male':
        m += 1
    else:
        b += 1
# Task №3
    age_ = item.get('age')
    if age_ > 30:
        names30_.append(item)
with open('names30.json','w') as f:
    json.dump(names30_,f, ensure_ascii=False, indent=4)
# Task № 2 (вывод ответа, написал после задания 3, чтобы не повторять команду with open as f: т.к. иначе пришлось бы в цикл запихнуть этот ответ и он бы выводился много раз..
print(f'Количество людей женского пола: {b}. Количество людей мужского пола: {m}')

# Task №4
import json

strawberry = []
banana = []
apple = []

with open('jjson.json', 'r') as f:
    file = json.load(f)
    for dictionaries in file:
        if dictionaries['favoriteFruit'] == 'strawberry':
            strawberry.append(dictionaries['name'])
        elif dictionaries['favoriteFruit'] == 'banana':
            banana.append(dictionaries['name'])
        elif dictionaries['favoriteFruit'] == 'apple':
            apple.append(dictionaries['name'])


print('People, who like strawberries:')
for i in range(len(strawberry)):
    print(str(i+1) + ')', strawberry[i])

print('\n')

print('People, who like apples:')
for i in range(len(apple)):
    print(str(i+1) + ')', apple[i])

print('\n')

print('People, who like bananas:')
for i in range(len(banana)):
    print(str(i+1) + ')', banana[i])








