import model
import view

def init():
    if not model.init(view.get_pb_name()):
        print(model.get_error())
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
            case 'i'|'I':
                lst = view.getRecord()
                model.insertRecord(lst)
            case 'd'|'D':
                num = model.getNumberOfRecords()
                if num != 0:
                    num = view.getNumberOfRecord(num)
                    model.deleteRecord(num)
            case 's'|'S':
                sOrder = view.getSortOrder()
                sField = view.getSortField()
                model.sortRecord(sOrder, sField)
        view.print_pb(model.read_db())
        cmd = view.getCommand()
    
            