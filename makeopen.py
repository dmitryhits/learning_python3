import builtins


def makeopen(id):
    original = builtins.open

    def custom(*pargs, **kargs):
        print("Custom open call %r" % id, pargs, kargs)
        return original(*pargs, **kargs)

    builtins.open = custom
