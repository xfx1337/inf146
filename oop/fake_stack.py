from queue import Queue

class Stack:
    def __init__(self):
        self.back_st = Queue()
        self.front_st = Queue()

    def push(self, el):
        self.front_st.push(el)

    def pop(self):
        while not self.front_st.is_empty:
            self.back_st.push(self.front_st.pop())
        el = self.back_st.pop()
        while not self.back_st.is_empty:
            self.front_st.push(self.back_st.pop())
        return el

    def peek(self):
        while not self.front_st.is_empty:
            self.back_st.push(self.front_st.pop())
        el = self.back_st.peek()
        while not self.back_st.is_empty:
            self.front_st.push(self.back_st.pop())
        return el
    
    @property
    def is_empty(self):
        return self.front_st.is_empty

q1 = Stack()
breakpoint()