# commuter.py

class Commuter1:
    def __init__(self, value = 0):
        self.data = value

    def __add__(self, other):
        print('add', self.data, other)
        return self.data + other

    def __radd__(self, other):
        print('radd', other, self.data)
        return other + self.data


class Commuter2:
    def __init__(self, value = 0):
        self.data = value

    def __add__(self, other):
        print('add', self.data, other)
        return self.data + other

    def __radd__(self, other):
        return self.__add__(other)     # call add explicitly


class Commuter3:
    def __init__(self, value = 0):
        self.data = value

    def __add__(self, other):
        print('add', self.data, other)
        return self.data + other

    def __radd__(self, other):
        return self + other             # swap and re-add


class Commuter4:
    def __init__(self, value = 0):
        self.data = value

    def __add__(self, other):
        print('add', self.data, other)
        return self.data + other

    __radd__ = __add__                 # alias, cuts out the middleman


class Commuter5:
    """ Propagate class type in the results"""
    def __init__(self, value = 0):
        self.data = value

    def __add__(self, other):
        if isinstance(other, Commuter5):        # Type test to avoid object nesting
            other = other.data
        return Commuter5(self.data + other)     # Else + result is another Commuter

    def __radd__(self, other):
        return Commuter5(other + self.data)

    def __str__(self):
        return '<Commuter5: %s>' % self.data


if __name__ == '__main__':
    for klass in (Commuter1, Commuter2, Commuter3, Commuter4, Commuter5):
        print('-'*60)
        x = klass(88)
        y = klass(99)

        print(x + 1)
        print(1 + y)
        print(x + y)



