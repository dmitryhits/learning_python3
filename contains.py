# contains.py


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):          # Fallback for iteration
        print('get %s[%s]:' % (self.__class__.__name__, i), end='')  # also for index, slice
        return self.data[i]

    def __iter__(self):                # Preferred for iterations
        print('iter=>', end='')        # allows only one active iterator
        self.ix = 0
        return self

    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x):        # Preferred for membership tests 'in'
        print('contains: ', end='')
        return x in self.data


if __name__ == '__main__':
    X = Iters([1, 2, 3, 4, 5])        # Make an instance
    print(3 in X)                     # Membership
    for i in X:                       # For loop
        print(i, end=' | ')

    print()                           # Other iteration contexts
    print([i**2 for i in X])
    print(list(map(bin, X)))

    I = iter(X)                       # Manual iteration
    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration:
            break
