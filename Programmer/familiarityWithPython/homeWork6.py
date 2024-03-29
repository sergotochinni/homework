from functools import reduce
import random

#from homeWork2.py
print("Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.")
n = int(input("Введите количество чисел: "))
#-------------------------------------------------------------------------------------------------
#l = []
#for x in range(1, n+1):
#    l.append((1+1/x)**x)
l = list(map(lambda x: ((1+1/x)**x), range(1, n+1)))
#-------------------------------------------------------------------------------------------------
#sum = 0
#for x in l:
#    sum += x
sum = reduce(lambda a,b: (a+b), l)
#-------------------------------------------------------------------------------------------------
print("Список: ", l)
print("Сумма = ", sum)
print()

#from homeWork2.py
print("Задайте список из N элементов, заполненных числами из промежутка [-N, N]. \
Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.")
n = int(input("Введите количество элементов: "))
#-------------------------------------------------------------------------------------------------
#l = []
#for x in range(-1*n, n+1):
#    l.append(x)
l = [x for x in range(-1*n, n+1)]
#-------------------------------------------------------------------------------------------------
print("Список: ", l)
s = input("Введите индексы элементов: ").split(" ")
m = 1
for x in s:
    m *= l[int(x)]
print("Произведение = ", m)

print()

#from homeWork3.py
#-------------------------------------------------------------------------------------------------
#def listGenerator(n):
#    l = []
#    for x in range(n):
#        l.append(random.randint(0, 10))
#    return l
def listGenerator(n):
    return [random.randint(0, 10) for x in range(n)]
#-------------------------------------------------------------------------------------------------

print(listGenerator(10))
print(listGenerator(7))

#from homeWork4.py
print("Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов \
исходной последовательности.")
random.seed()
n = int(input("Enter a number: "))
if n < 0:
    print("Negative value of the number of numbers!")
else:
    l = listGenerator(n)
    print("List: ", l)
#-------------------------------------------------------------------------------------------------
#    m = []
#    for x in l:
#        if l.count(x) == 1:
#            m.append(x)
    m = list(filter(lambda x: l.count(x) == 1, l))
#-------------------------------------------------------------------------------------------------
    print("Non repeated: ", m)

print()