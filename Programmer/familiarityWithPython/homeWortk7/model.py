import os

#переменная с текстом ошибки для возвращения по запросу
error = ''
#db_type = 0 # 0-none, 1-txt, 2-csv, 3-sql
db_file = ''
db_data = []
#возвращает текст ошибки
def get_error() -> str:
    return error

#в зависимости от типа файла инициализирует соответствующие функции чтения/записи
#вход: имя файла
#выход: true или false
def init(file_name: str) -> bool:
    global error
    global db_file
    global db_data
    if not os.path.exists(file_name):
        print(f'File {file_name} not found.')
        s = input('Create? (Y/N)')
        if s == 'Y' or s == 'y':
            f = open(file_name, 'w')
            f.write('McMillan\nTricia\n267709\nSection ZZ9 Plural Z Alpha\n\n')
            f.write('Dent\nArthur\n267709\nSection ZZ9 Plural Z Alpha\n\n')
            f.write('Ford\nPrefect\n1234567890\nBetelgeuse\n\n')
            f.write('VeryVeryLongSurName\nVeryVeryLongName\n3.14159265359\nVeryVeryVeryVeryLongComment\n\n')
            f.close()
        else:
            error = 'File not found.'
            return False
    # match os.path.split(file_name)[1]:
    #     case 'txt':
    #         db_type = 1
    #         print('txt init')
    #     case 'csv':
    #         db_type = 2
    #         print('csv init')
    #     case 'db':
    #         db_type = 3
    #         print('sql init')
    #     case _:
    #         error = 'Error file type.'
    #         return False
    db_file = file_name
    f = open(db_file, 'r')
    while True:
        surname = f.readline().strip()
        if not surname:
            break
        name = f.readline().strip()
        tel = f.readline().strip()
        comment = f.readline().strip()
        endOfRecord = f.readline().strip()
        db_data.append([surname, name, tel, comment, endOfRecord])
    f.close()
    return True

def read_db() -> list:
    return db_data

def write_db():
    f = open(db_file, 'w')
    for x in db_data:
        f.write('\n'.join(x)+'\n')
    f.close()
    return

def changeRecord(num, lst):
    db_data[num-1] = lst
    write_db()
    return
    
def deleteRecord(num):
    del db_data[num-1]
    write_db()
    return

def insertRecord(lst):
    if lst[0] =='' and lst[1] == '':
        return
    for x in db_data:
        if x[0] == lst[0] and x[1] == lst[1] and x[2] == lst[2] and x[3] == lst[3]:
            return
    db_data.append(lst)
    write_db()
    return

def sortSurname(e):
    return e[0]

def sortName(e):
    return e[1]

def sortComment(e):
    return e[3]

def sortRecord(sortOrder, sortField):
    if sortField == 's': sortFunc = sortSurname
    if sortField == 'n': sortFunc = sortName
    if sortField == 'c': sortFunc = sortComment
    db_data.sort(reverse=sortOrder, key=sortFunc)
    return

def getRecord(num) -> list:
    return db_data[num-1]

def getNumberOfRecords() -> int:
    return len(db_data)