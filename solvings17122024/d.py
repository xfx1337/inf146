class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def swap_pairs(head: Node) -> Node:
    temp = Node()
    temp.next = head
    prev = temp

    while prev.next != None and prev.next.next != None:
        f = prev.next
        s = prev.next.next
        
        prev.next = s
        f.next = s.next
        s.next = f
        
        prev = f

    return temp.next

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
            return i
        while True:
            if cur.next != None:
                cur = cur.next
            else:
                return i
            i += 1

l1 = map(int, "1 2 3 4 5 6 7 8 9 10".split())

l1l = LinkedList()

for el in l1:
    l1l.append(el)
x = swap_pairs(l1l.head)
breakpoint()