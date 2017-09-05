#!python
# listinherited.py

class ListInherited:
    """
    Use dir() to collect both instance attrs and names inherited
    from its classes; Python 3.X shows more names than 2.X because
    of the implied object superclass in the new style class model;
    getattr() fetches inherited names not in self.__dict__;
    use __str__ and not __repr__ or else it loops when printing bound methods
    """
    def __attrnames(self):
        result = ''
        for attr in dir(self):                                      # instance dir
            if attr[:2] == '__' and attr[-2:] == '__':              # skip internals
                result += '\t%s\n' % attr
            else:
                result += '\t%s=%s\n' % (attr, getattr(self,attr))
        return result

    def __str__(self):
        return 'Instance of %s, address %s\n%s' % (
            self.__class__.__name__,                                # class name
            id(self),                                               # address
            self.__attrnames()                                      # name = value list
        )


if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInherited)
