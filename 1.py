x = input('Введите сумму чисел:').split('+')
y = int(x[0]) + int(x[1]) + int(x[2])
print(y)
print(x)
y = 0
index = 0
for i in x:
    y += int(x[index])
    index += 1
print(y)

