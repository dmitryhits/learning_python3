class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances += 1

    def printNumberofInstances():
        print('Number of instance created: %s' % Spam.numInstances)
