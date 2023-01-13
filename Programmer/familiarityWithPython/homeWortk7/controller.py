import logger
import model
import view

def init():
    logger.init()
    if not model.init(view.get_pb_name()):
        err = model.get_error()
        print(err)
        logger.writeToLog(err)
        exit()
    view.print_pb(model.read_db())

def run():
    cmd = view.getCommand()
    while cmd not in ['q', 'Q']:
        match cmd:
            case 'v'|'V':
                num = model.getNumberOfRecords()
                if num != 0:
                    num = view.getNumberOfRecord(num)
                    view.viewRecord(model.getRecord(num))
                    view.pressEnter()
            case 'c'|'C':
                num = model.getNumberOfRecords()
                if num != 0:
                    num = view.getNumberOfRecord(num)
                    lst = view.getRecord(model.getRecord(num))
                    model.changeRecord(num, lst)
                    logger.writeToLog(f'Changed record number {num}: ' + ';'.join(lst))
            case 'i'|'I':
                lst = view.getRecord(['','','',''])
                model.insertRecord(lst)
                logger.writeToLog('Inserted record: ' + ';'.join(lst))
            case 'd'|'D':
                num = model.getNumberOfRecords()
                if num != 0:
                    num = view.getNumberOfRecord(num)
                    model.deleteRecord(num)
                    logger.writeToLog(f'Deleted record number {num}.')
            case 's'|'S':
                sOrder = view.getSortOrder()
                sField = view.getSortField()
                model.sortRecord(sOrder, sField)
        view.print_pb(model.read_db())
        cmd = view.getCommand()
    
            