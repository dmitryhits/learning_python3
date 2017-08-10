# private0.py


class PrivateExc(Exception):
    pass


class Privacy:
    def __setattr__(self, attrname, value):              # On self.attrname = value
        if attrname in self.privates:
            raise PrivateExc(attrname, self)             # Make, raise user-defined exception
        else:
            self.__dict__[attrname] = value              # Avoid loops by using dictionary


class Test1(Privacy):
    privates = ['age']


class Test2(Privacy):
    privates = ['name', 'pay']

    def __init__(self):
        self.__dict__['name'] = 'Tom'

if __name__ == '__main__':
    x = Test1()
    y = Test2()

    x.name = 'Bob'
    # y.name = 'Sue' # falis
    print(x.name)
    print(y.name)

    y.age = 30
    # x.age = 40    # fails
    print(y.age)
