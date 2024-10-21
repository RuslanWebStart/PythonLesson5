# -*- coding: cp1251 -*-

# Урок 5

# Задание 1
number = float(input('Введите число: '))

if number > 0:
    if number % 2 == 0:
        print('Положительное четное число')
    else:
        print('Положительное нечетное число')
elif number < 0:
    if number % 2 == 0:
        print('Отрицательное четное число')
    else:
        print('Отрицательное нечетное число')
else:
    print('Нулевое число')


# Задание 2
word = input('Введите слово в нижнем регистре: ')

'a e i o u y'
a = word.count('a')
e = word.count('e')
i = word.count('i')
o = word.count('o')
u = word.count('u')
y = word.count('y')

if a == 0:
    print("a = False")
if e == 0:
    print("e = False")
if i == 0:
    print("i = False")
if o == 0:
    print("o = False")
if u == 0:
    print("u = False")
if y == 0:
    print("y = False")

print('Гласных: ',a + e + i + o + u + y)
print('Согласных: ',len(word) - (a + e + i + o + u + y))


# Задание 3
Mike = float(input('Mike, введите сумму для инвестиций: '))
Ivan = float(input('Ivan, введите сумму для инвестиций: '))
minX = float(input('Введите минимальную сумму для инвестиций: '))

if Mike >= minX or Ivan >= minX:
    if Mike >= minX:
        print('Mike')
    if Ivan >= minX:
        print('Ivan')
if Mike < minX and Ivan < minX and (Mike + Ivan) >= minX:
    print(1)
if Mike >= minX and Ivan >= minX:
    print(2)
if Mike < minX and Ivan < minX and (Mike + Ivan) <minX:
    print(0)