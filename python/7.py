from math import *


def prime(x):
    for i in range(3, x-1, 2):
        if x % i == 0:
            return False
    return True


def decomp(x, fac):
    for i in range(fac):
        if fac % x**i != 0:
            return i-1


def decompose(number):
    fac = factorial(number)

    print('2^' + str(decomp(2, fac)), end='')
    for i in range(3, number+1, 2):
        if prime(i) == True:
            e = decomp(i, fac)
            if e != 1:
                print(' * ' + str(i) + '^' + str(e), end='')
            else:
                print(' * ' + str(i), end='')
        else:
            continue

    print('\n')


decompose(22)
