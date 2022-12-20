import random
from os import path

print("Напишите программу, удаляющую из текста все слова, содержащие 'абв'. \
В тексте используется разделитель пробел.")
random.seed()
n = int(input('Enter number of words: ') or 10)
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


def encode(plain):
    enc = ''
    cnt = 0
    sym = plain[0]
    for c in plain:
        if c == sym:
            cnt += 1
        else: #if
            enc += str(cnt) + sym
            sym = c
            cnt = 1
    else: #for
            enc += str(cnt) + sym
    return enc

def decode(enc):
    plain = ''
    num = ''
    for c in enc:
        if c.isdigit():
            num += c
        else:
            plain += c * int(num)
            num = ''
    return plain

print('Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. \
Входные и выходные данные хранятся в отдельных текстовых файлах.')
fin = input('Enter the name of the file with the text (default: text_words.txt): ') or 'text_words.txt'
fout = input('Enter the file name to record (default: text_code_words.txt): ') or  'text_code_words.txt'
fdec = input( 'Enter the name of the file to decode (default: text_code_words.txt): ') or  'text_code_words.txt'

if path.exists(fin):
    fi = open(fin, 'r')
    plainText = fi.readlines()
    fi.close()
    plainText = list(map(str.rstrip, plainText))
    with open(fout, 'w') as fo:
        encodedText = list(map(encode, plainText))
        for i in range(len(encodedText)):
            print('Plain   text: ',plainText[i])
            print('Encoded text: ', encodedText[i])
            fo.write(encodedText[i] + '\n')
else:
    print(f'Error. File {fin} not found.')

if path.exists(fdec):
    fd = open(fdec, 'r')
    encText = fd.readlines()
    fd.close()
    encText = list(map(str.rstrip, encText))
    decText = list(map(decode, encText))
    for i in range(len(decText)):
        print('Encoded text: ', encText[i])
        print('Decoded text: ', decText[i])
else:
    print(f'Error. File {fdec} not found.')

print()

