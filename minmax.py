print("I am:" , __name__)

def minmax(test, *args):
    res = args[0]
    for arg in args:
        if test(arg,res):
            res =arg
    return res

def lessthan(x,y):return x<y
def greaterthan(x,y):return x>y


if __name__ == '__main__':
    print(minmax(lessthan, 1,2,3,5,7,8,9))
    print(minmax(greaterthan, 1,2,3,5,7,8,9))