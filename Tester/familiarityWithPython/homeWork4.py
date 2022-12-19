import os
import random
from decimal import Decimal, ROUND_HALF_UP 

# разбор строки с полиномом, на выходе список, где индекс - это степень, значение - это коэффициент.
def parsePolynom(st):
    k = 0
    power = 0
    sign = 1
    s = ''
    koeffs = []
    for x in st:
        match x:
            case '=':
                if k == 0:
                    k = sign * int(s)
                    power = 0
                else:
                    power = int(s)
                koeffs[power] = k
                break
            case '*' | '^' | ' ':
                pass
            case 'x':
                k = sign * int(s)
                s = ''
            case '+' | '-':
                power = int(s)
                if len(koeffs) == 0:
                    koeffs = [0 for i in range(power+1)]
                koeffs[power] = k
                s = ''
                k = 0
                sign = 44 - ord(x)
            case _:
                s += x
    return koeffs

# генератор списка длинной n, значения заполняются случайным числом от 0 до 9
def listGenerator(n):
    l = []
    for x in range(n):
        l.append(random.randint(0, 10))
    return l

# на входе натуральная степень, на выходе строка сполиномом, количество и значения коэффициентов выбираются случайным образом
def makePolynom(k):
    random.seed()
    polynom = ""
    # for p = k, k-1, .. 2
    for p in range(k, 0, -1):
        n = random.randint(0, 9)
        if abs(n) >= 1:
            polynom += str(n) + "*x^" + str(p) + random.choice([' + ',' - '])
# for p = 1
#n = random.randint(0, 9)
#if abs(n) >= 1:
#    polinom += str(n) + "*x" + ")"
# for p = 0
# if all p = 0
    if len(polynom) < 2:
        polynom = str(random.randint(2, 9)) + "*x^1" + random.choice([' + ', ' - ']) + str(random.randint(2, 9))
    else:
        n = random.randint(0, 9)
        if n != 0:
            polynom += str(n)
        else:
            polynom = polynom[:-3]
    polynom += " = 0"
    return polynom

# на входе список, где индекс - это степень, значение - это коэффициет, на выходе строка с полиномом
def makePolynomFromList(lst):
    polynom = ""
    for p in range(len(lst)-1, 0, -1):
        n = lst[p]
        if p == len(lst)-1:
            polynom += str(n) + "*x^" + str(p)
        else:
            if n > 0:
                polynom += ' + ' + str(n) + "*x^" + str(p)
            if n < 0:
                polynom += ' - ' + str(abs(n)) + "*x^" + str(p)
    n = lst[0]
    if n > 0:
        polynom += ' + ' + str(n)
    if n < 0:
        polynom += ' - ' + str(abs(n))
    polynom += " = 0"
    return polynom

#1
print("Вычислить число c заданной точностью d")
n = Decimal(input("Enter a real number: "))
d = Decimal(input("Enter the required accuracy '0.0001': "))
print(n.quantize(d, ROUND_HALF_UP))

print()

#2
print("Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.")
n = int(input("Enter a number: "))
l = []
d = 2
while n !=1:
    if n % d == 0:
        l.append(d)
        n /= d
    else:
        d += 1
print(l)

print()

#3
print("Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов \
исходной последовательности.")
random.seed()
n = int(input("Enter a number: "))
if n < 0:
    print("Negative value of the number of numbers!")
else:
    l = listGenerator(n)
    print("List: ", l)
    m = []
    for x in l:
        if l.count(x) == 1:
            m.append(x)
    print("Non repeated: ", m)

print()

#4
print("Задана натуральная степень k. \
Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, \
записать в файл полученный многочлен не менее 3-х раз.")
f = open('polynom.txt', 'w')
for x in range(3):
    k = int(input("Enter a power of natural number: "))
    plnm = makePolynom(k)
    f.write(plnm)
    f.write('\n')
    print(plnm)
f.close()
print('All write to polynom.txt')

print()

#5
print('Даны два файла, в каждом из которых находится запись многочленов. \
Задача - сформировать файл, содержащий сумму многочленов.')
if os.path.exists('poly.txt') == False or os.path.exists('poly_2.txt') == False:
    print('poly.txt or poly_2.txt not found. Generate...')
    f1 = open('poly.txt', 'w')
    f2 = open('poly_2.txt', 'w')
    for i in range(0, random.randint(3,10)):
        f1.write(makePolynom(random.randint(0, 10)))
        f2.write(makePolynom(random.randint(0, 10)))
        f1.write('\n')
        f2.write('\n')
    f1.close()
    f2.close()

f1 = open('poly.txt', 'r')
f2 = open('poly_2.txt', 'r')
p1 = f1.readlines()
p2 = f2.readlines()
f1.close()
f2.close()

if len(p1) == len(p2):
    f1 = open('poly_sum.txt', 'w')
    for i in range(len(p1)):
        k1 = parsePolynom(p1[i])
        k2 = parsePolynom(p2[i])
        if len(k1) < len(k2):
            k1, k2 = k2, k1
        for j in range(len(k2)):
            k1[j] += k2[j]
        print('First  polynom:', p1[i], end='')
        print('Second polynom:', p2[i], end='')
        plnm = makePolynomFromList(k1)
        print('Sum of polynoms:', plnm,'\n')
        f1.write(plnm)
        f1.write('\n')
    print('All write to poly_sum.txt')
    f1.close()
else:
    print('The contents of the files do not match!')
