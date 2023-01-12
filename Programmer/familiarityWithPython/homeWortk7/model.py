import os
import sqlite3

#переменная с текстом ошибки для возвращения по запросу
error = ''
db_type = '' #txt, csv, sql
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
    global db_type
    if not os.path.exists(file_name):
        print(f'File {file_name} not found.')
        s = input('Create? (Y/N)')
        if s == 'Y' or s == 'y':
            if os.path.splitext(file_name)[1] == '.txt':
                f = open(file_name, 'w')
                f.write('McMillan\nTricia\n267709\nSection ZZ9 Plural Z Alpha\n\n')
                f.write('Dent\nArthur\n267709\nSection ZZ9 Plural Z Alpha\n\n')
                f.write('Ford\nPrefect\n1234567890\nBetelgeuse\n\n')
                f.write('VeryVeryLongSurName\nVeryVeryLongName\n3.14159265359\nVeryVeryVeryVeryLongComment\n\n')
                f.close()
            if os.path.splitext(file_name)[1] == '.csv':
                f = open(file_name, 'w')
                f.write('McMillan;Tricia;267709;Section ZZ9 Plural Z Alpha\n')
                f.write('Dent;Arthur;267709;Section ZZ9 Plural Z Alpha\n')
                f.write('Ford;Prefect;1234567890;Betelgeuse\n')
                f.write('VeryVeryLongSurName;VeryVeryLongName;3.14159265359;VeryVeryVeryVeryLongComment\n')
                f.close()
            if os.path.splitext(file_name)[1] == '.sqlite':
                f = sqlite3.connect(file_name)
                create_users_table = """
                                    CREATE TABLE users (
                                        surname TEXT,
                                        name TEXT,
                                        phone TEXT,
                                        comment TEXT);
                                    """
                cursor = f.cursor()
                cursor.execute(create_users_table)
                f.commit()
                create_users = """
                                INSERT INTO
                                    users (surname, name, phone, comment)
                                VALUES
                                    ('McMillan', 'Tricia', '267709', 'Section ZZ9 Plural Z Alpha'),
                                    ('Dent', 'Arthur', '267709', 'Section ZZ9 Plural Z Alpha'),
                                    ('Ford', 'Prefect', '1234567890', 'Betelgeuse'),
                                    ('VeryVeryLongSurName', 'VeryVeryLongName', '3.14159265359', 'VeryVeryVeryVeryLongComment');
                                """
                cursor = f.cursor()
                cursor.execute(create_users)
                f.commit()
                cursor.close()
                f.close()
        else:
            error = 'File not found.'
            return False
    db_file = file_name
    match os.path.splitext(file_name):
        case *path, '.txt':
            db_type = 'txt'
            db_data = readDbFromTxt()
            print('txt init')
        case *path, '.csv':
            db_type = 'csv'
            db_data = readDbFromCsv()
            print('csv init')
        case *path, '.sqlite':
            db_type = 'sqlite'
            db_data = readDbFromSqlite()
            print('sql init')
        case _:
            error = 'Error file type.'
            return False
    return True

def readDbFromTxt() -> list:
    db = []
    f = open(db_file, 'r')
    while True:
        surname = f.readline().strip()
        if not surname:
            break
        name = f.readline().strip()
        tel = f.readline().strip()
        comment = f.readline().strip()
        endOfRecord = f.readline().strip()
        db.append([surname, name, tel, comment])
    f.close()
    return db

def readDbFromCsv() -> list:
    db = []
    f = open(db_file, 'r')
    for x in f:
        lst = x.strip('\n').split(';')
        db.append(lst)
    f.close()
    return db

def readDbFromSqlite() -> list:
    db = []
    f = sqlite3.connect(db_file)
    select_users = "SELECT * FROM users;"
    cursor = f.cursor()
    cursor.execute(select_users)
    db = list(cursor.fetchall())
    cursor.close()
    f.close()
    return db

def read_db() -> list:
    return db_data

def write_db():
    if db_type == 'txt':
        f = open(db_file, 'w')
        for x in db_data:
            f.write('\n'.join(x)+'\n\n')
        f.close()
    if db_type == 'csv':
        f = open(db_file, 'w')
        for x in db_data:
            f.write(';'.join(x)+'\n')
        f.close()
    if db_type == 'sqlite':
        f = sqlite3.connect(db_file)
        create_users_table = """
                            CREATE TABLE users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            surname TEXT,
                            name TEXT,
                            phone TEXT,
                            comment TEXT);
                            """
        delete_all_from_users = "DELETE FROM users;"

        cursor = f.cursor()
        cursor.execute(delete_all_from_users)
        f.commit()
        create_users = """
                        INSERT INTO
                            users (surname, name, phone, comment)
                        VALUES 
                        """ + ','.join(str(tuple(x)) for x in db_data) + ';'
        cursor = f.cursor()
        cursor.execute(create_users)
        f.commit()

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