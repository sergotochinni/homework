import excep
import logg
import model_op as operation


def menu():
    print('Calculator welcomes you!\n')
    while True:
        logg.logging.info('Start menu.')
        print('Working with:\n'
                '1 - rational\n'
                '2 - complex\n'
                '0 - exit')
        command = input()
        if command not in ['1', '2', '0']:
            print('Try again!')
            logg.logging.warning('Main menu, wrong item selected.')
            continue
        if command == '0': good_buy()
 
        logg.logging.info('Start menu calc. With rational.')
        op = get_operation()
        if op == '0': 
            logg.logging.info('Stop menu calc.')
            continue
 
        if command == '1':
            n1str = input('Enter 1 number: ')
            n2str = '0'
            if op != '6': n2str = input('Enter 2 number: ')
            n1, n2, checked = excep.check_in(n1str, n2str)
        else:
            n1_real_str = input('Enter 1 real part: ')
            n1_img_str = input('Enter 1 imaginary part: ')
            n2_real_str = '0'
            n2_img_str = '0'
            if op != '6': 
                n2_real_str = input('Enter 2 real part: ')
                n2_img_str = input('Enter 2 imaginary part: ')
            n1, n2, checked = excep.check_in_complex(n1_img_str, n1_real_str, n2_img_str, n2_real_str)
 
        if not checked: 
            print('Incorrect data entered.')
            logg.logging.info('Stop menu calc.')
            continue
 
        if op == '4':
            if excep.check_zero(n2):
                print('Can`t divide by zero!')
                continue
            elif command == '1':
                logg.logging.info('Start menu div.')
                op = get_div()
                if op == '0': 
                    logg.logging.info('Stop menu div.')
                    continue
                if op == '1': op = '4'
                if op == '2': op = '7'
                if op == '3': op = '8'
                logg.logging.info('Stop menu div.')
 
        match op:
            case '1':
                print(operation.sub(n1, n2))
            case '2':
                print(operation.sum(n1, n2))
            case '3':
                print(operation.mul(n1, n2))
            case '4':
                print(operation.div1(n1, n2))
            case '5':
                print(operation.pow(n1, n2))
            case '6':
                print(operation.sqrt(n1))
            case '7':
                print(operation.div2(n1, n2))
            case '8':
                print(operation.div3(n1, n2))
        logg.logging.info('Stop menu calc.')


def good_buy():
    logg.logging.info('Stop program.')
    print('Buy buy!')
    exit()


def get_operation():
    print('Operations:\n'
            '1 - sub\n'
            '2 - sum\n'
            '3 - mul\n'
            '4 - div\n'
            '5 - pow\n'
            '6 - sqrt\n'
            '0 - previous menu')
    command = input()
    while command not in ['1', '2', '3', '4', '5', '6', '0']:
        logg.logging.warning('Wrong item selected.')
        print('Try again!')
        command = input()
    return command


def get_div():
    print('Operations:\n'
            '1 - /\n'
            '2 - //\n'
            '3 - %\n'
            '0 - previous menu')
    command = input()
    while command not in ['1', '2', '3', '0']:
        logg.logging.warning('Wrong item selected.')
        print('Try again!')
        command = input()
    return command