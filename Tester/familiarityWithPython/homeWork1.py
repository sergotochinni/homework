from math import sqrt
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.
print("Является ли день выходным.")
dow = int(input("Номер дня недели: "))
if dow == 6 or dow == 7:
    print("Да")
else:
    if dow > 0 and dow < 6:
        print("Нет")
    else:
        print("Ошибка")
print()

# Напишите программу для. проверки истинности утверждения (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.
print("Проверка истинности выражения.")
for x in (True, False):
    for y in (True, False):
        for z in (True, False):
            for w in (True, False):
                print("( "+str(w)+" ⋀ "+str(z)+" ) ⋁ ¬ "+str(y)+" ⋁ ( ¬ "+str(x)+" ≡ ¬ "+str(w)+" )  \t",end="")
                if ((w and z) or not y or (not x == (not w))):
                    print("Истина")
                else:
                    print("Ложь")
print()

# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
print("Номер четверти плоскости, в которой находится эта точка.")
x = int(input("X: "))
y = int(input("Y: "))
if x == 0 or y == 0:
    print("Ошибка")
else:
    print("Четверть № ", end="")
    if x > 0:
        if y > 0:
            print(1)
        else:
            print(4)
    else:
        if y > 0:
            print(2)
        else:
            print(3)
print()

# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
print("показывает диапазон возможных координат точек в четверти (x и y)")
c = int(input("Четверть номер № "))
if c < 1 or c > 4:
    print("нет такой четверти")
else:
    print("Диапазон возможных координат: ", end="")
    if c == 1:
        print("(0..∞), (0..∞)")
    if c == 2:
        print("-(0..∞), (0..∞)")
    if c == 3:
        print("-(0..∞), -(0..∞)")
    if c == 4:
        print("(0..∞), -(0..∞)")
print()

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
print("Расстояние между точками.")
x1 = int(input("Точка1 X: "))
y1 = int(input("Точка1 Y: "))
x2 = int(input("Точка2 X: "))
y2 = int(input("Точка2 Y: "))
print("Расстояние между точками: %.3f" % sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)))