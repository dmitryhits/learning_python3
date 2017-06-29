from functools import reduce #used in fact2
import math #used in fact4



def fact1(N = 10):
    if N>1:
        return N*fact1(N-1)
    else:
        return 1


def fact2(N = 10):
    return reduce((lambda x,y: x * y),range(1,N+1))


def fact3(N = 10):
    res = 1
    for i in range(N):
        res *= (i+1)
    return res


def fact4(N = 10):
    return math.factorial(N)

