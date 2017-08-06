# manynames.py

X = 11                  # Global variable (module X)


def f():
    print(X)            # Access global variable


def g():
    X = 22              # Local function variable (hides module X)
    print(X)


class C:
    X = 33              # Class attribute (C.X)

    def m(self):
        X = 44          # Local variable in method (X)
        self.X = 55     # Instance variable (instance.X)


if __name__ == '__main__':
    print(X)
    f()
    g()
    print(X)

    obj = C()
    print(obj.X)

    obj.m()
    print(obj.X)
    print(C.X)
