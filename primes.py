def prime0(y):
    x = abs(y)//2
    while x>1:
        if y%x == 0:
            print(y, 'has factor', x)
            break
        x-=1
    else:
        print(y, 'is prime')


prime0(-13)
prime0(13.)
prime0(-15)
prime0(15.)
prime0(0)
