# trace.py


class Wrapper:
    def __init__(self, obj):
        self.wrapped = obj

    def __getattr__(self, attrname):
        print('Trace:', attrname)
        return getattr(self.wrapped, attrname)
