L = []
for x in range(7):
    L.append(2**x)
X=6
if 2**X in L:
    print('at index', L.index(2 ** X))
else:
    print('Not found')

