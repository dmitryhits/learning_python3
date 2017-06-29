def countdown(x):
    if x == 0:
        print('STOP')
    else:
        print(x)
        x-=1
        countdown(x)

countdown(10)