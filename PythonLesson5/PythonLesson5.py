# -*- coding: cp1251 -*-

# ���� 5

# ������� 1
number = float(input('������� �����: '))

if number > 0:
    if number % 2 == 0:
        print('������������� ������ �����')
    else:
        print('������������� �������� �����')
elif number < 0:
    if number % 2 == 0:
        print('������������� ������ �����')
    else:
        print('������������� �������� �����')
else:
    print('������� �����')


# ������� 2
word = input('������� ����� � ������ ��������: ')

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

print('�������: ',a + e + i + o + u + y)
print('���������: ',len(word) - (a + e + i + o + u + y))


# ������� 3
Mike = float(input('Mike, ������� ����� ��� ����������: '))
Ivan = float(input('Ivan, ������� ����� ��� ����������: '))
minX = float(input('������� ����������� ����� ��� ����������: '))

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