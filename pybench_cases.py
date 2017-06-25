"""
pybench_cases.py: run pybench on a set of pythons and statements.

Select modes by editting this script or using command-line arguments
(in sys.argv): e.g., run a "pypy pybench_cases.py" to test just one specific version
on stmts, "pybench_case.py -a" to test all pythons listed, "python pybench_cases.py -a -t"
to trace command lines too.
"""

import pybench, sys

pythons = [            # (ispy3, path)
    (1, 'python'),     # default on anaconda
    (0, 'pypy'),
    (0, 'py2')
]

stmts = [ # (num, rpt, stmt)
    (0, 0, "[x**2 for x in range(1000)]"), #iterations
    (0, 0, "res = []\nfor x in range(1000): res.append(x**2)"), #multistmt
    (0, 0, "$listif3(map(lambda x: x**2, range(1000)))"),
    (0, 0, "list(x**2 for x in range(1000))"),
    (0, 0, "s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"), #str ops
    (0, 0, "s = '?'\nfor i in range(10000): s +='?'"),
]

tracecmd = '-t' in sys.argv # -t trace command lines
pythons = pythons if '-a' in sys.argv else None # All in the list else one
pybench.runner(stmts, pythons, tracecmd)



