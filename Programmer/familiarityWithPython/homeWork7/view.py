#получение от пользователя имени файла с базой данных
def get_pb_name() -> str:
    db_name = ''
    while db_name == '': #ждем пока хоть что-нибудь не введет
        db_name = input('Enter file name (*.txt, *.csv or *.sqlite default: phone_book.txt): ') or 'phone_book.txt'
    return db_name

# печать на экран всей адресной книги
def print_pb(lst):
    # начало телефонно книги, ширина вывода на экран 80 символов
    print('='*80)
    # переменная для нумерации записей
    i = 0
    for x in lst:
        i += 1
        # если длина данных больше ширины поля для вывода, данные обрезаются, в конец добавляется многоточие.
        # для фамилии ширина поля 15 символов
        surname = x[0] if len(x[0]) <= 15 else x[0][:12]+'...'
        # для имени ширина поля 15 символов
        name = x[1] if len(x[1]) <= 15 else x[1][:12]+'...'
        # для телефона ширина поля 12 символов
        phone = x[2] if len(x[2]) <= 12 else x[2][:9]+'...'
        # для комментария ширина поля 26 символов
        comment = x[3] if len(x[3]) <= 26 else x[3][:23]+'...'
        # для номера записи ширина поля 2 символа
        print(f'|{i:>2}| {surname:<15}| {name:<15}|{phone:>12} | {comment:<26}|')
    # конец телефонной книги
    print('='*80)
    
# получение команды от пользователя    
def getCommand() -> str:
    while True: # ждем пока не введет нормальную команду
        st = input('Enter command (v - view, c - change, i - insert, d - delete, s - sort, e - export, q - quit): ')
        if st in ['v', 'c', 'i', 'd', 's', 'e', 'q', 'V', 'C', 'I', 'D', 'S', 'E', 'Q']:
            return st

# получение от пользователя номера записи, для функций изменения или удаления
# в numOfRecords задается количество записей в телефонной книге, чтобы ввел только из диапазона 1..numOfRecords
def getNumberOfRecord(numOfRecords: int) -> int:
    if numOfRecords == 0:
        return 0
    n = int(input(f'Enter number of record from 1 to {numOfRecords}: '))
    while n<1 or n>numOfRecords:
        n = int(input(f'Enter number of record from 1 to {numOfRecords}: '))
    return n

# пауза до нажатия Enter
def pressEnter():
    m = input('Press Enter')
    print()
    return

# вывод на экран одной записи
def viewRecord(lst: list):
    print('='*80)
    print(f'Surname: {lst[0]}')
    print(f'Name: {lst[1]}')
    print(f'Phone: {lst[2]}')
    print(f'Comment: {lst[3]}')
    print('='*80)

# получение от пользователя новой записи
# на вход подается ['', '', '', ''] или заполненый, чтобы заново все не вводить
def getRecord(lst: list) -> list:
    lst[0] = input(f'Enter new surname ({lst[0]}): ') or lst[0]
    lst[1] = input(f'Enter new name ({lst[1]}): ') or lst[1]
    lst[2] = input(f'Enter new phone ({lst[2]}): ') or lst[2]
    lst[3] = input(f'Enter new comment ({lst[3]}): ') or lst[3]
    return lst

# получение порядка сортировки
def getSortOrder() -> bool:
    n = input('Enter the sort type (a - ascending, d - descending): ') or 'a'
    if n == 'd' or n == 'D':
        return True
    return False

# получение значения по какому полю сортировать
def getSortField() -> str:
    n = input('Enter the field of sort (s - surname, n - name, c - comment): ') or 's'
    if n not in ['s', 'n', 'c']:
        n = 's'
    return n

def getExport() -> str:
    while True: # ждем пока не введет нормальную команду
        st = input('Enter type for export (t - txt, c - csv, s - sql, q - quit): ')
        if st in ['t', 'c', 's', 'q', 'T', 'C', 'S', 'Q']:
            return st
