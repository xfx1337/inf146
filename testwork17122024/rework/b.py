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


def removeElements(head: Node, val) -> None:
    if head is None: return head
    cur = head.next
    last = head
    while cur != None:
        if cur.data == val:
            last.next = cur.next
            cur = last.next
        else:
            last = cur
            cur = cur.next
    if head.data == val:
        head = head.next
    return head
