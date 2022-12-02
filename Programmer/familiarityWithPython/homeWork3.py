import random

def listGenerator(n):
    l = []
    for x in range(n):
        l.append(random.randint(0, 10))
    return l

random.seed()
print("Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,\
 стоящих на нечётной идексах.")
l = listGenerator(random.randint(5, 25))
print("List: ", l)
s = 0
for x in range(1, len(l), 2):
    s += l[x]
print("Summ: ", s)

print()

print("Напишите программу, которая найдёт произведение пар чисел списка. \
    Парой считаем первый и последний элемент, второй и предпоследний и т.д.")
l = listGenerator(random.randint(5, 25))
print("List: ", l)
m = []
mid = len(l)//2 + len(l)%2
for x in range(mid):
    m.append(l[x]*l[len(l)-1-x])
print("Mul: ", m)

print()

print("Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу \
между максимальным и минимальным значением дробной части элементов.")
n = random.randint(5, 25)
l = []
for x in range(n):
    l.append(round(random.uniform(0, 10), 5))
print("List: ", l)
min = l[0]%1
max = l[1]%1
for x in l:
    if x%1 > max:
        max = x%1
    if x%1 < min:
        min = x%1
print("Answer:", max-min) 

print()

print("Напишите программу, которая будет преобразовывать десятичное число в двоичное.")
n = int(input("Введите десятичное число: "))
s = ""
while n > 0:
    s = str(n%2) + s
    n //= 2
print("Двоичное: ", s)

print()

print("Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.")
def fib(n):
    lp = []
    ln = []
    for x in range(n+1):
        if x==0 or x==1:
            lp.append(x)
            ln.append(x)
        else:
            lp.append(lp[x-1]+lp[x-2])
            ln.append(ln[x-2]-ln[x-1])
    ln.reverse()
    ln.extend(lp[1:])
    return ln

n = int(input("Введите число: "))
print(fib(n))