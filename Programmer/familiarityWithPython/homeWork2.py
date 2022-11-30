print("Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.")
s = input("Введите число: ")
s = s.replace('.', '', 1) 
s = s.replace(',', '', 1) 
m = 0
if s.isdigit():
    for x in s:
        m = m + int(x)
    print("Сумма всех цифр:", m)
else:
    print("Это не число.")

print()

print("Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.")
n = int(input("Введите число: "))
l = []
for x in range(1,n+1):
    m = 1
    for y in range(1,x+1):
        m = m * y
    l.append(m)
print(l)

print()

print("Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.")
n = int(input("Введите количество чисел: "))
l = []
for x in range(1, n+1):
    l.append((1+1/x)**x)

sum = 0
for x in l:
    sum += x
print("Список: ", l)
print("Сумма = ", sum)

print()

print("Задайте список из N элементов, заполненных числами из промежутка [-N, N]. \
Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.")
n = int(input("Введите количество элементов: "))
l = []
for x in range(-1*n, n+1):
    l.append(x)
print("Список: ", l)
s = input("Введите индексы элементов: ").split(" ")
m = 1
for x in s:
    m *= l[int(x)]
print("Произведение = ", m)

print()

import random
print("Реализуйте алгоритм перемешивания списка.")
n = int(input("Введите длину списка: "))
l = []
for x in range(n):
    l.append(x)
print("Список: ", l)
random.seed()
for x in range(len(l)):
    i = random.randint(0,len(l)-1)
    j = random.randint(0,len(l)-1)
    l[i], l[j] = l[j], l[i]
print("Перемешаный список: ", l)
