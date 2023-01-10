#получение имени файла с базой данных
def get_pb_name() -> str:
    db_name = ''
    while db_name == '':
        db_name = input('Enter file name (default: phone_book.txt): ') or 'phone_book.txt'
    return db_name

def print_pb(lst):
    print('='*80)
    i = 0
    for x in lst:
        i += 1
        surname = x[0] if len(x[0]) <= 15 else x[0][:12]+'...'
        name = x[1] if len(x[1]) <= 15 else x[1][:12]+'...'
        phone = x[2] if len(x[2]) <= 12 else x[2][:9]+'...'
        comment = x[3] if len(x[3]) <= 26 else x[3][:23]+'...'
        print(f'|{i:>2}| {surname:<15}| {name:<15}|{phone:>12} | {comment:<26}|')
    print('='*80)
    
def getCommand() -> str:
    while True:
        st = input('Enter command (v - view, c - change, i - insert, d - delete, s - sort, q - quit): ')
        if st in ['v', 'c', 'i', 'd', 's', 'q', 'V', 'C', 'I', 'D', 'S', 'Q']:
            return st

def getNumberOfRecord(numOfRecords) -> int:
    if numOfRecords == 0:
        return 0
    n = int(input(f'Enter number of record from 1 to {numOfRecords}: '))
    while n<1 or n>numOfRecords:
        n = int(input(f'Enter number of record from 1 to {numOfRecords}: '))
    return n

def pressEnter():
    m = input('Press Enter')
    print()
    return

def viewRecord(lst):
    print('='*80)
    print(f'Surname: {lst[0]}')
    print(f'Name: {lst[1]}')
    print(f'Phone: {lst[2]}')
    print(f'Comment: {lst[3]}')
    print('='*80)

def getRecord(lst=['','','','']) -> list:
    lst[0] = input(f'Enter new surname ({lst[0]}): ') or lst[0]
    lst[1] = input(f'Enter new name ({lst[1]}): ') or lst[1]
    lst[2] = input(f'Enter new phone ({lst[2]}): ') or lst[2]
    lst[3] = input(f'Enter new comment ({lst[3]}): ') or lst[3]
    return lst

def getSortOrder() -> bool:
    n = input('Enter the sort type (a - ascending, d - descending): ') or 'a'
    if n == 'd' or n == 'D':
        return True
    return False

def getSortField() -> str:
    n = input('Enter the field of sort (s - surname, n - name, c - comment): ') or 's'
    if n not in ['s', 'n', 'c']:
        n = 's'
    return n