import os
import sqlite3


#переменная с текстом ошибки для возвращения по запросу
error = ''
# переменная для хранения типа базы данных
db_type = '' #txt, csv, sqlite
# для хранения имени файла базы данных
db_file = ''
# для хранения данных считанных из базы данных
db_data = []

db_data_test = [['McMillan', 'Tricia', '267709', 'Section ZZ9 Plural Z Alpha'],
                ['Dent', 'Arthur', '267709', 'Section ZZ9 Plural Z Alpha'],
                ['Ford','Prefect', '1234567890', 'Betelgeuse'],
                ['VeryVeryLongSurName', 'VeryVeryLongName', '3.14159265359', 'VeryVeryVeryVeryLongComment']]

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

    db_file = file_name
    # проверка существования путии файла
    if not os.path.exists(file_name):
        print(f'File {file_name} not found.')
        # если файл не найден, то спросить, создать или нет с тестовыми данными
        s = input('Create? (Y/N)')
        if s == 'Y' or s == 'y':
            # в зависимости от расширения введенного имени файла переменные инициализаруются соответствующим кодом
            match os.path.splitext(file_name):
                case *path, '.txt':
                    db_type = 'txt'
                case *path, '.csv':
                    db_type = 'csv'
                case *path, '.sqlite':
                    db_type = 'sqlite'
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
                    cursor.close()
                    f.close()
                case _:
                    error = 'Error file type.'
                    return False
            db_data = db_data_test
            write_db()
        else: # если файл не найден и пользователь отказался создавать новый
            error = 'File not found.'
            return False 
    # читаем из файла записи
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

# чтение записей из текстового файла, формат записей:
# Фамилия_1
# Имя_1
# Телефон_1
# Описание_1
# 
# Фамилия_2
# Имя_2
# Телефон_2
# Описание_2
# 

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

# чтение записей из csv файла, формат записей:
# Фамилия_1;Имя_1;Телефон_1;Описание_1
# Фамилия_2;Имя_2;Телефон_2;Описание_2
def readDbFromCsv() -> list:
    db = []
    f = open(db_file, 'r')
    for x in f:
        lst = x.strip('\n').split(';')
        db.append(lst)
    f.close()
    return db

# чтение записей из файла базы данных
def readDbFromSqlite() -> list:
    db = []
    f = sqlite3.connect(db_file)
    select_users = "SELECT * FROM users;"
    cursor = f.cursor()
    cursor.execute(select_users)
    for x in cursor.fetchall():
        db.append(list(x))
    cursor.close()
    f.close()
    return db

# возвращает всю телефонную книгу
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

# изменить запись по порядковому номеру
def changeRecord(num, lst):
    # изменить запись
    db_data[num-1] = lst
    # записать в файл
    write_db()
    return

# удалить запись из телефонной книги по порядковому номеру    
def deleteRecord(num):
    # удалить запись из базы
    del db_data[num-1]
    # записать в файл
    write_db()
    return

# вставляет запись в телефонную книгу
def insertRecord(lst):
    # поле фамилия или имя обязательно должно быть
    if lst[0] =='' and lst[1] == '':
        return
    # проверка, что запись уже есть, чтобы не задваивались
    for x in db_data:
        if x[0] == lst[0] and x[1] == lst[1] and x[2] == lst[2] and x[3] == lst[3]:
            return
    # добавить запись в базу
    db_data.append(lst)
    # записать базу в файл
    write_db()
    return

# сортирует по полю фамилия
def sortSurname(e):
    return e[0]

# сортирует по полю имя
def sortName(e):
    return e[1]

# сортирует по полю комментарий
def sortComment(e):
    return e[3]

# функция сортировки записей
def sortRecord(sortOrder, sortField):
    if sortField == 's': sortFunc = sortSurname
    if sortField == 'n': sortFunc = sortName
    if sortField == 'c': sortFunc = sortComment
    db_data.sort(reverse=sortOrder, key=sortFunc)
    return

# функция для получения данных конкретной записи, указанной пономеру
def getRecord(num) -> list:
    return db_data[num-1]

# функция для получения количества записей в телефонной книге
def getNumberOfRecords() -> int:
    return len(db_data)

def export(ts: str):
    global db_file
    global db_type

    db_file_org = db_file
    db_type_org = db_type
    db_file = os.path.splitext(db_file)[0]
    match ts:
        case 't':
            db_type = 'txt'
            db_file += '.txt'
        case 'c':
            db_type = 'csv'
            db_file += '.csv'
        case 's':
            db_type = 'sqlite'
            db_file += '.sqlite'
            f = sqlite3.connect(db_file)
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
            cursor.close()
            f.close()
    write_db()
    db_file = db_file_org
    db_type = db_type_org
