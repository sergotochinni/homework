import random

print('1. Представлен список чисел. Необходимо вывести элементы исходного списка, \
значения которых больше предыдущего элемента. Use comprehension.')
n = int(input('Enter a number: '))
lst1 = [random.randint(0, 100) for x in range(n)]
lst2 = [lst1[i] for i in range(1, len(lst1)) if lst1[i]>lst1[i-1]]
print(lst1)
print(lst2)

print()

print('2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.')
n = int(input('Enter a upper limit: '))
lst = [x for x in range(20, n+1) if x%20 == 0 or x%21 == 0]
print(lst)

print()

def convertNames(listNames):
    listNames.sort()
    m = {}
    for x in lst:
        if x[0] in m:
            m[x[0]].append(x)
        else:
            m[x[0]] = [x]
    return m

print('3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, \
значения — списки, содержащие имена, начинающиеся с соответствующей буквы.')
lst =  ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]
print(lst)
print(convertNames(lst))

print()

def groupToSur(listPeoples):
    m = {}
    for x in listPeoples:
        idx = x.find(' ')+1
        if x[idx] in m:
            if x[0] in m[x[idx]]:
                m[x[idx]][x[0]].append(x)
            else:
                m[x[idx]][x[0]] = [x]
        else:
            m[x[idx]] = {x[0] : [x]}
    return m
print('4. Функция принимает в качестве аргументов строки в формате «Имя Фамилия», \
возвращает словарь, ключи — первые буквы фамилий, значения — словари, реализованные по схеме предыдущего задания.')
lst = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Юнона Ветрякова", "Борис Аркадьев", "Антон Серов", "Павел Анисимов"]
print(lst)
listN = groupToSur(lst)
print(listN)

print()

print('5. Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)')
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
n = int(input('Enter a number: '))
print([(' ').join([nouns[random.randint(0,4)], adverbs[random.randint(0,4)],adjectives[random.randint(0,4)]]) for x in range(n)])