class Deque:
    def __init__(self):
        self._queue = []
    
    def push_back(self, element):
        self._queue.append(element)
    def push_front(self, element):
        self._queue.insert(0, element)

    def pop_front(self):
        if not self.empty():
            element = self._queue[0]
            del self._queue[0]
            return element     

    def pop_back(self):
        if not self.empty():
            element = self._queue[-1]
            del self._queue[-1]
            return element  
    
    def empty(self):
        return len(self._queue) == 0
    
    def clear(self):
        self._queue = []