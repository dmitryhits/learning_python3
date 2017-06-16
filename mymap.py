# map(func, seq, ...) workalike with zip

def mymap1(func, *seq):
    res = []
    for args in zip(*seq):
        res.append(func(*args))
    return res


print("map1", mymap1(abs, [-2, -1, 0, 1, 2]))
print("map1", mymap1(pow, [1, 2, 3], [2, 3, 4, 5]))


def mymap2(func, *seq):
    return [func(*args) for args in zip(*seq)]


print('map2', mymap2(abs, [-2, -1, 0, 1, 2]))
print('map2', mymap2(pow, [1, 2, 3], [2, 3, 4, 5]))

def mymap3(func, *seq):
    for args in zip(*seq):
        yield func(*args)


print('map3', list(mymap3(abs, [-2, -1, 0, 1, 2])))
print('map3', list(mymap3(pow, [1, 2, 3], [2, 3, 4, 5])))

def mymap4(func, *seq):
    return (func(*args) for args in zip(*seq))

print('map4', list(mymap4(abs, [-2, -1, 0, 1, 2])))
print('map4', list(mymap4(pow, [1, 2, 3], [2, 3, 4, 5])))

#zip(seq...) and 2.X  map(None, seq ...) workalike

def myzip1(*seqs):
    print(seqs)
    [print(S) for S in seqs]
    seqs = [list(S) for S in seqs]
    print(*seqs)
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res

def mymapPad1(*seqs, pad = None):
    seqs = [list(S) for S in seqs]
    res = []
    while any(seqs):
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res

S1,S2 = 'abc', 'xyz123'
print('myzip1', myzip1(S1,S2))
print('mymapPad1', mymapPad1(S1,S2))
print('mymapPad1', mymapPad1(S1,S2, pad=99))

#using generators: yield

def myzip2(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)


def mymapPad2(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)

S1,S2 = 'abc', 'xyz123'
print('myzip2', list(myzip2(S1,S2)))
print('mymapPad2', list(mymapPad2(S1,S2)))
print('mymapPad2', list(mymapPad2(S1,S2, pad=99)))


# Alternative implementation with lengths

def myzip3(*seqs):
    minlen = min(len(S) for S in seqs)
    return [tuple(S[i] for S in seqs) for i in range(minlen)]

def mymapPad3(*seqs,pad=None):
        maxlen = max(len(S) for S in seqs)
        return [tuple((S[i] if len(S)>i else pad) for S in seqs) for i in range(maxlen)]

S1,S2 = 'abc', 'xyz123'
print('myzip3', myzip3(S1,S2))
print('mymapPad3', mymapPad3(S1,S2))
print('mymapPad3', mymapPad3(S1,S2, pad=99))

# Alternative with lengths and generators

def myzip4(*seqs):
    minlen = min(len(S) for S in seqs)
    return (tuple(S[i] for S in seqs) for i in range(minlen))

S1,S2 = 'abc', 'xyz123'
print('myzip4', list(myzip4(S1,S2)))


