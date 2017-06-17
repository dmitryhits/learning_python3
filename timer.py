''' 
Home grown timing tool for function calls
Does total time, best-of time, and best-of-totals time
'''

import time, sys

timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(reps, func, *pargs, **kargs):
    """
    Total time to run func reps times
    Returns total time and last result
    :param reps: Number of times to run the function
    :param func: function name
    :param pargs: optional positional arguments passed to the function
    :param kargs: optional keyword arguments to the fuction
    :return: total time, last result
    """
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        result = func(*pargs, **kargs)
    elapsed = timer()-start
    return (elapsed, result)

def bestof(reps, func, *pargs, **kargs):
    """
    Quickest func() among reps runs
    Returns the best time, last result
    """
    best = 2*32
    for i in range(reps):
        start = timer()
        result = func(*pargs, **kargs)
        elapsed = timer()-start
        if elapsed<best: best=elapsed
    return (best, result)

def bestoftotal(reps1,reps2,func, *pargs, **kargs):
    """
    best of totals
    Best of reps1 runs of (total reps2 runs of func() )
    """
    return total(reps1,total, reps2, func, *pargs, **kargs)