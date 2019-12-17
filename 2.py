year = int(input('Введите год: '))
if year % 400 == 0 or year % 4 == 0:
    print('Год високосный')
elif year % 100 == 0 and year % 400 > 0:
    print('Год не високосный')
else: print('Год не високосный')