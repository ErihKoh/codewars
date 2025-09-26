import sys
from decimal import *

setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN))
int = Decimal
sys.set_int_max_str_digits(10 ** 7)


def sum_strings(x, y):
    return str(int(x or '0') + int(y or '0'))


if __name__ == '__main__':
    x = '1'
    y = '3'
    print(sum_strings(x, y))
