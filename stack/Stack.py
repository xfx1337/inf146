class Stack:
    def __init__(self):
        self._stack = []
    
    def push(self, x):
        self._stack.append(x)

    def pop(self):
        if not self.is_empty:
            c = self._stack[-1]
            del self._stack[-1]
            return c
    # def pop(self):
    #     return self._stack.pop()
    
    def peek(self):
        if not self.is_empty:
            return self._stack[-1]

    @property
    def is_empty(self):
        return len(self._stack) == 0
