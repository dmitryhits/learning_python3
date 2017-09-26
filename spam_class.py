class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances += 1

    def printNumberofInstances(cls):
        print('Number of instance created: %s %s' % (cls.numInstances, cls))
    printNumberofInstances = classmethod(printNumberofInstances)


class Sub(Spam):
    def printNumberofInstances(cls):
        print('Extra stuff ...', cls)
        Spam.printNumberofInstances()
    printNumberofInstances = classmethod(printNumberofInstances)


class Other(Spam):
    pass
