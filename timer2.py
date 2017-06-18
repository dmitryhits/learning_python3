"""
total(spam, 1, 2, a=3, b=4, _reps=1000) calls and times spam(1, 2, a=3, b=4) 
_reps times and returns total time for all runs and the final result

bestof(spam, 1, 2, a=3, b=4, _reps=5) runs best-of-N timer to attemt to filter out system
load variation, and return the best time out of _reps tests

bestoftotal(spam, 1, 2, a=3, b=4, _reps1=5, _reps=1000) runs best-of-totals test, which takes 
best among _reps1 runs of (the total of _reps runs)
"""

import time, sys

if sys.version_info[0]>=3 and sys.version_info[1]>=3:
    timer = time.perf_counter
else:
    timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(func, *pargs, **kargs):
    _reps=kargs.pop('_reps', 1000)
    repslist = list(range(_reps))
    start = timer()
    for i in repslist:
        result = func(*pargs, **kargs)
    elapsed = timer()-start
    return (elapsed, result)

def bestof(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000)
    best = 2*32
    for i in range(_reps):
        start = timer()
        result = func(*pargs, **kargs)
        elapsed = timer()-start
        if elapsed<best: best=elapsed
    return (best, result)

def bestoftotal(func, *pargs, **kargs):
    _reps1 = kargs.pop('_reps1', 5)
    return min(total(total,func, *pargs, **kargs) for i in range(_reps1))
