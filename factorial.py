from functools import reduce #used in fact2
import math #used in fact4


#recursive function call
def fact1(N = 10):
    if N>1:
        return N*fact1(N-1)
    else:
        return 1

#reduce lambda
def fact2(N = 10):
    return reduce((lambda x,y: x * y),range(1,N+1))

#loop
def fact3(N = 10):
    res = 1
    for i in range(N):
        res *= (i+1)
    return res

# built-in function (the fastest way to calculate factorial
def fact4(N = 10):
    return math.factorial(N)

