import random

print("Напишите программу, удаляющую из текста все слова, содержащие 'абв'. \
В тексте используется разделитель пробел.")
random.seed()
n = int(input('Enter number of words: '))
txt = ''
for x in range(n):
    lst = ['а', 'б', 'в']
    for y in range(len(lst)):
        letter = random.choice(lst)
        lst.remove(letter)
        txt += letter
    txt += ' ' 
#txt = input("Enter text: ")
#txt = 'абв кабв абвк кабвк бва www'
print('Source text: ', txt)
txt = txt.split(" ")
txt = list(filter(lambda x: x.find('абв')<0 , txt))
print('Filtered text: ', (' ').join(txt))

print()
