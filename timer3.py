#3.x only
"""
Same usage as timer2.py but uses 3.X keyword only arguments 
instead of dict pop method for simpler code. No need to hoist range 
out of tests: always a generator in 3.X and this cann't run in 2.X
"""

import time, sys

if sys.version_info[0]>=3 and sys.version_info[1]>=3:
    timer = time.perf_counter
else:
    timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(func, *pargs, _reps = 1000, **kargs):
    start = timer()
    for i in range(_reps):
        res = func(*pargs, **kargs)
    elapsed = timer() - start
    return (res, elapsed)


def bestof(func, *pargs, _reps = 5, **kargs):
    best = 2**32
    for i in range(_reps):
        start = timer()
        res = func(*pargs, *kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, res)


def bestoftotal(func, *pargs, _reps1=5, **kargs):
    return min(total(func, *pargs, **kargs) for i in range(_reps1))