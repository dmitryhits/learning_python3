#!python
"""
reloadall.py: transitively reload nested modules (2.X and 3.X)
Call reloadall with one or more imported modules.
"""


import types
from importlib import reload


def status(module):
    print('reloading ', module.__name__)


def tryreload(module):
    try:
        reload(module)
    except:
        print('FAILED: %s' % module)


def transitive_reload(module, visited):
    if not module in visited:                              # trap cycles, duplicates
        status(module)                                     # Reload this module
        tryreload(module)                                  # And visit children
        visited[module] = True
        for attrobj in module.__dict__.values():
            if type(attrobj) == types.ModuleType:          # Recursive if module
                #print('In module %s' % module.__name__)
                transitive_reload(attrobj, visited)


def reload_all(*args):
    visited = {}                                           # Main entry point
    for arg in args:                                       # for all passed in
        #print(arg)
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)


def tester(reloader, modname):                              # Self test code
    import importlib, sys                                   # import on tests only
    if len(sys.argv) > 1: modname = sys.argv[1]             # command line or passed
    #print('testing:', modname)
    module = importlib.import_module(modname)               # Import by name string
    reloader(module)                                        # Test passed-in reloader


if __name__ == '__main__':
    tester(reload_all, 'reloadall')                         # Test: reload myself?


