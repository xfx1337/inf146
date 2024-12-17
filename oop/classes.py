class Test:
    def __init__(self): # constructor
        pass
    
    def __add__(self, a): # b + a: will do for b: self + a
        pass
    
    def __radd__(self, a): # reverse. will do self + b
        pass
    
    def __rsub__(self, a):
        pass
    
    def __call__(self, args):
        pass

    def __getattr__(self, atr):
        pass

    def __getitem__(self, key): #Test[key]
        pass # like dict
    
    def __setitem__(self, key, value): #Test[key] = 2
        pass 