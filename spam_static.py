class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances += 1

    def printNumberofInstances():
        print('Number of instance created: %s' % Spam.numInstances)
    printNumberofInstances = staticmethod(printNumberofInstances)


class Sub(Spam):
    def printNumberofInstances():                                         # override the staticmethod
        print("Extra stuff ...")
        Spam.printNumberofInstances()                                     # but call back to the original
    printNumberofInstances = staticmethod(printNumberofInstances)

