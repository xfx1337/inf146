class Queue:
    def __init__(self):
        self._queue = []
    
    def push(self, el):
        self._queue.append(el)
    
    def pop(self):
        # if not self.is_empty:
        #     el = self.peek()
        #     del self.queue[0]
        #     return el
        if not self.is_empty:
            return self._queue.pop(0)        

    def peek(self):
        return self._queue[0]
    
    @property
    def is_empty(self):
        return len(self._queue) == 0