"""
pybench_cases2.py: run pybench on a set of pythons and statements.

Select modes by editting this script or using command-line arguments
(in sys.argv): e.g., run a "pypy pybench_cases.py" to test just one specific version
on stmts, "pybench_case.py -a" to test all pythons listed, "python pybench_cases.py -a -t"
to trace command lines too.
"""

import pybench, sys

pythons = [
    (1, 'python'),
    (0, 'pypy')
]

stmts = [
    # Use function calls
    (0, 0, "[ord(x) for x in 'spam' * 2500]"),
    (0, 0, "res = []\nfor x in 'spam' * 2500: res.append(ord(x))"),
    (0, 0, "$listif3(map(ord,'spam' * 2500))"),
    (0, 0, "list(ord(x) for x in 'spam' * 2500)"),
    # Sets and dictionaries
    (0, 0, "{x**2 for x in range(1000)}"),
    (0, 0, "s = set()\nfor x in range(1000): s.add(x**2)"),
    (0, 0, "{x:x**2 for x in range(1000)}"),
    (0, 0, "d = {}\nfor x in range(1000): d[x] = x**2"),
    #Pathological case: 300k digits
    (1, 1, "len(str(2**1000000))")
]

tracecmd = '-t' in sys.argv # -t trace command lines
pythons = pythons if '-a' in sys.argv else None # All in the list else one
pybench.runner(stmts, pythons, tracecmd)