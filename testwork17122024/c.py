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

def deleteDuplicates(head: Node) -> Node:
    if head == None:
        return head
    cur = head
    while cur.next != None:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head
        
l1 = list(map(int, "1 1 2 2 2 3 4 5 6 7 7 8".split()))

l1l = LinkedList()
for el in l1:
    l1l.append(el)
x = l1l.head
x = deleteDuplicates(None)
breakpoint()