class Operation:
    def __init__(self, function, name, priority):
        self.function = function
        self.name = name
        self.priority = priority
    
    def __call__(self, *args):
        return self.function(*args)

    def __str__(self):
        return "opertation1"
    
    def __repr__(self):
        return "memory?"

o = Operation(lambda a,b: a+b, "sum", 0)
print(o(1,2))