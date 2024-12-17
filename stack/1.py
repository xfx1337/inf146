#LIFO Last In First Out

from Stack import Stack


x = Stack()
print(x.is_empty)
x.push(1)
x.push(2)
print(x.is_empty)
print(x.peek())
print(x.pop())
print(x.pop())
print(x.is_empty)
breakpoint()