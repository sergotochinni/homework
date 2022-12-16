print("Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.")
f = float(input("Введите число: "))

s = 0
w = f%1
q = f//1

n = 0
w1 = round(w, n)
while (q + w1) != f:
    n += 1
    w1 = round(w, n)

w = w1 * 10**n

while q != 0:
    s += q % 10
    q //= 10

while w != 0:
    s += w % 10
    w //= 10

print("Сумма всех цифр:", s)

print()

print("Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N в виде списка.")
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

print("Напишите программу, которая принимает на вход 2 числа.\
Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].\
Найдите произведение элементов на указанных позициях(не индексах).")
n = int(input("Enter the value of N: "))
l = []
for x in range(-1*n, n+1):
    l.append(x)
print("List: ", l)
p1 = int(input("Position one: "))
p2 = int(input("Position two: "))
if p1<1 or p2<1 or p1>n*2+1 or p2>n*2+1:
    print("There are no values for these indexes!")
else:
    print("Mul: ", l[p1-1]*l[p2-1])
print()

import random
print("Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.")
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
