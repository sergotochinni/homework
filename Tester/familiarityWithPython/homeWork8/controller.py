import logger
import model
import view

def init():
    #  инициализация логгера
    logger.init()
    # если инициализация базы данных прошла с ошибкой, то записать в лог и завершить работу
    if not model.init(view.get_pb_name()):
        err = model.get_error()
        print(err)
        logger.writeToLog(err)
        exit()
    # вывести на экран телефонную книгу
    view.print_pb(model.read_db())

def run():
    # получаем команду от пользователя
    cm = view.getCommand()
    # цикл выполняется пока не будет введен символ q или Q
    while cm not in ['q', 'Q']:
        match cm:
            # просмотреть одну запись
            case 'v'|'V':
                # получить количество записей в телефонной книге
                num = model.getNumberOfRecords()
                # если в телефонной книге нет записей, то ничего не делать
                if num != 0:
                    # получить номер записи для просмотра
                    num = view.getNumberOfRecord(num)
                    # вывести на экран данные
                    view.viewRecord(model.getRecord(num))
                    # подождать нажатия клавиши Enter, после нажатия снова выведется вся телефонная книга
                    view.pressEnter()
            # изменить одну запись
            case 'c'|'C':
                # получить количество записей в телефонной книге
                num = model.getNumberOfRecords()
                # если в телефонной книге нет записей, то ничего не делать
                if num != 0:
                    # получить номер записи для редактирования
                    num = view.getNumberOfRecord(num)
                    # получить изменяемую запись и передать в функцию для получения данных,
                    # чтобы не писать заново те поля, которые не надо менять, а просто нажать Enter
                    lst = view.getRecord(model.getRecord(num))
                    # изменить данные в телефонной книге
                    model.changeRecord(num, lst)
                    # записать в лог
                    logger.writeToLog(f'Changed record number {num}: ' + ';'.join(lst))
            # вставить запись
            case 'i'|'I':
                # получить данные для добавления в телефонную книгу
                lst = view.getRecord(['','','',''])
                # добавить данные в телефонную книгу
                model.insertRecord(lst)
                # записать в лог
                logger.writeToLog('Inserted record: ' + ';'.join(lst))
            # удалить запись
            case 'd'|'D':
                # получить количество записей в телефонной книге
                num = model.getNumberOfRecords()
                # если в телефонной книге нет записей, то ничего не делать
                if num != 0:
                    # получить номер записи для удаления
                    num = view.getNumberOfRecord(num)
                    # удалить запись
                    model.deleteRecord(num)
                    # записать в лог
                    logger.writeToLog(f'Deleted record number {num}.')
            # отсортировать телефонную книгу
            case 's'|'S':
                # получить порядок сортировки
                sOrder = view.getSortOrder()
                # получит поле по которому сортировать
                sField = view.getSortField()
                # отсортировать
                model.sortRecord(sOrder, sField)
            case 'e'|'E':
                ts = view.getExport()
                if ts not in ['q', 'Q']:
                    model.export(ts)
        # вывести на экран телефонную книгу
        view.print_pb(model.read_db())
        cm = view.getCommand()
    
            