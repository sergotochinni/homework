import cmath
import math
import logg


def sub(x1, x2):
    res = x1 - x2
    logg.logging.info(f'Sub: {x1} - {x2} = {res}')
    return res


def sum(x1, x2):
    res = x1 + x2
    logg.logging.info(f'Sum: {x1} + {x2} = {res}')
    return res


def mul(x1, x2):
    res = x1 * x2
    logg.logging.info(f'Mul: {x1} * {x2} = {res}')
    return res


def div1(x1, x2):
    res = x1 / x2
    logg.logging.info(f'Div /: {x1} * {x2} = {res}')
    return res


def div2(x1, x2):
    res = x1 // x2
    logg.logging.info(f'Div //: {x1} * {x2} = {res}')
    return res


def div3(x1, x2):
    res = x1 % x2
    logg.logging.info(f'Div %: {x1} * {x2} = {res}')
    return res


def pow(x1, x2):
    res = x1 ** x2
    logg.logging.info(f'Pow: {x1} ** {x2} = {res}')
    return res


def sqrt(x1):
    if str(type(x1)) == "<class 'complex'>":
        res = cmath.sqrt(x1)
    else:
        res = math.sqrt(x1)
    logg.logging.info(f'Sqrt: {x1} ^ 2 = {res}')
    return res
