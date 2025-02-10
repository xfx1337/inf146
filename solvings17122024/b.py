class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.empty():
            c = self.stack[-1]
            del self.stack[-1]
            return c
    
    def peek(self):
        if not self.empty():
            return self.stack[-1]
            
    def empty(self):
        return len(self.stack) == 0


s = input().split()

st = Stack()
for i in s:
    if i in "+-*/":
        oper = i
        b = st.pop()
        a = st.pop()
        st.push(f"({a}{oper}{b})")
    else:
        st.push(i)
print(st.pop())