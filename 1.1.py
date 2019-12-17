list_1 = input('Введите набор чисел через пробел: ').split(' ')
i = 0
for a in list_1:
    list_1[i] = int(a)
    i += 1
print(max(list_1))

print(list_1[3])
