"""
reloadall3.py: transitively reload nested modules (nested stack)
"""


import types
from reloadall import status, tryreload, tester


def transitive_reload(modules, visited):
    while modules:
        nextmod = modules.pop()
        status(nextmod)
        tryreload(nextmod)
        visited.add(nextmod)
        #print('VISITED:', visited)
        modules.extend(x for x in nextmod.__dict__.values()
                       if type(x) == types.ModuleType and x not in visited and x not in modules)
        #print('MODULES;', modules)


def reload_all(*modules):
    transitive_reload(list(modules), set())


if __name__ == '__main__':
    tester(reload_all, 'reloadall3')
