import random
from os import path

print("1. Напишите программу, удаляющую из текста все слова, содержащие 'абв'. \
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

print('2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. \
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

def printTable(lst):
    print('      ---------------------')
    for i in range(0, 7, 3):
        print(f'\t{lst[i+1]}\t{lst[i+2]}\t{lst[i+3]} ')
        print('      ---------------------')
    print('')

def getMove(gamer, table):
    while True:
        p = input(f'Select a position {gamer}? ')
        if len(p) > 1 or len(p) == 0:
            print('Incorrect input \U000026D4. Are you sure you entered a correct number?')
        elif p < '1' or p > '9':
            print('Incorrect input \U000026D4. Are you sure you entered a correct number?')
        elif table[int(p)] != 0:
            print('This cell is already ocuppied\U0001F937')
        else:
            return int(p)
    
print('3. Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.')
gamerX = '\U0000274C'
gamerO = '\U00002B55'
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
pos = [0 for i in range(10)]
printTable(lst)
whoseMove = 'X'
for i in range(9):
    print('Enter a number from 1 to 9.')
    if whoseMove == 'X':
        move = getMove(gamerX, pos)
        lst[move] = gamerX
        pos[move] = 1
        whoseMove = 'O'
    else:
        correctInput = False
        move = getMove(gamerO, pos)
        lst[move] = gamerO
        pos[move] = -1
        whoseMove = 'X'
    printTable(lst)
    win = [pos[1]+pos[2]+pos[3], pos[4]+pos[5]+pos[6], pos[7]+pos[8]+pos[9], pos[1]+pos[4]+pos[7], pos[2]+pos[5]+pos[8], \
    pos[3]+pos[6]+pos[9], pos[1]+pos[5]+pos[9], pos[3]+pos[5]+pos[7]]
    if 3 in win:
        print(f'{gamerX} - WIN!')
        break
    if -3 in win:
        print(f'{gamerO} - WIN!')
        break
else:
    print('Drawn game!')

print()

print('4. Создайте программу для игры с конфетами человек против человека. \
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. \
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. \
Все конфеты оппонента достаются сделавшему последний ход. \
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?')
bot = int(input('Play with bot 1 - yes, 0 - no? '))
if bot:
    print('1 player - human, 2 playr - bot')
else:
    print('1 player - human, 2 playr - person')
sweets = 2021
max = sweets
limit = 28
win = False
firstMove = True
player = 'human'
move = 0
while not win:
    print(f'There are {sweets} sweets on the table, you can take [1..{limit}]')
    print(f'Player {player}`s move.')
    correctMove = False
    while not correctMove:
        if player == 'bot':
            playerMove = move
            if firstMove:
                firstMove = False
                if move > max % (limit+1):
                    move = limit + 1 - move
                else:
                    move = max % (limit+1) - move    
            else:
                move = limit + 1 - move
            if move == 0:
                move = random.randint(1, limit)
                max = max - playerMove - move
                firstMove = True
            print(f'The {player} took {move} candies')
        else:
            move = int(input(f'How many candies do you want {player}: '))
        if move > limit or move > sweets or move <=0:
            print('Incorrect input \U000026D4. Are you sure you entered a correct number?')
        else:
            correctMove = True
    sweets -= move
    if sweets == 0:
        print(f'The player {player} won!')
        win = True
    if player == 'human':
        if bot:
            player = 'bot'
        else:
            player = 'person'
    else:
        player = 'human'
