def adder(**kargs):
    if kargs:
        keylist = list(kargs.keys())
        res = kargs[keylist[0]]
        for k in keylist[1:]:
            res += kargs[k]
        return res


print(adder(a = 2, b = 3, c = 5))
print(adder(a ='spam', b = 'ham', c = 'dram'))
print(adder(a = 1.234))
print(adder(a = [1, 2, 3], b = [4, 5, 6], c = [0, 1, 0]))
print(adder())
