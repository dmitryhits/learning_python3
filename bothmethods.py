# bothmethods.py
class Methods:
    def imeth(self,x):                           # Normal instance method passed as self
        print([self, x])

    def smeth(x):                                # Static method: no instance passed
        print([x])

    def cmeth(cls, x):                           # Class method: get class not an instance
        print([cls,x])

smeth = staticmethod(smeth)                      # Make smeth static method
cmeth = classmethod(cmeth)                       # Make cmeth class method
