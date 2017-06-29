"Test relative speed of iteration tools alternatives"

import sys, timer2, math

reps = 10000
replist = list(range(reps))
#test function
def F(x): return math.sqrt(x)

def forLoop():
    res = []
    for x in replist:
        res.append(F(x))
    return res


def listComp():
    return [F(x) for x in replist]


def mapCall():
    return list(map(F,replist))


def genExpr():
    return list(F(x) for x in replist)


def genFunc():
    def gen():
        for x in replist:
            yield F(x)
    return list(gen())




print(sys.version)


for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (total, result) = timer2.bestoftotal(test, _reps1=5, _reps=1000)
    print('%-9s: %.5f => [%s...%s]' %
          (test.__name__, total, result[0], result[-1]))