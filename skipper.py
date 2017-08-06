#!python3
# skipper.py


class SkipObject:
    def __init__(self, wrapped):                 # save the new value to be used
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)        # new iterator each time


class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped                   # iterator state information
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):     # terminate iterations
            raise StopIteration
        else:
            item = self.wrapped[self.offset]      # else return and skip
            self.offset += 2
            return item

if __name__ == '__main__':
    alpha = 'abcdefg'
    skipper = SkipObject(alpha)                    # make container object
    I = iter(skipper)                              # make iterator on it
    print(next(I), next(I), next(I))               # visit offsets 0, 2, 4

    for x in skipper:                              # for call __iter__ automatically
        for y in skipper:                          # nested fors call iterator each time again
            print(x + y, end=" ")                  # each iterator has its own state, offset
