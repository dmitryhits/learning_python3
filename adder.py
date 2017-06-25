def adder(*argp):
    if argp:
        res = argp[0]
        for x in argp[1:]:
            res += x
        return res

print(adder(2, 3, 5, 6, 7, 8))
print(adder('spam', 'ham', 'dram'))
print(adder('spam'))
print(adder(1.234))
print(adder([1, 2, 3], [4, 5, 6], [0, 1, 0]))
print(adder())
