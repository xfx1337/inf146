class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def __getitem__(self, key):
        i = 0
        cur = self.head
        while i < key:
            next = cur.next
            if next != None:
                cur = cur.next
                i += 1
            else:
                raise ValueError("cannot find")

        return cur.data
    
    def append(self, data):
        cur = self.head
        if cur.data == None:
            cur.data = data
            return
        while True:
            if cur.next != None:
                cur = cur.next
            else:
                cur.next = Node(data)
                break
    
    @property
    def length(self):
        cur = self.head
        i = 1
        if cur.data == None:
            cur.data = data
            return i
        while True:
            if cur.next != None:
                cur = cur.next
            else:
                return i
            i += 1

def removeElements(head: Node, val) -> Node:
    last = head
    cur = head.next
    while cur != None:
        if cur.data == val:
            last.next = cur.next
        elif cur == None:
            break
        last = cur
        cur = cur.next
    if head.data == val:
        head = head.next


l1 = list(map(int, "1 0 234 1 0 7 1".split()))

l1l = LinkedList()
for el in l1:
    l1l.append(el)
x = l1l.head
removeElements(x, 1)
breakpoint()