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

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def mergeTwoLists(list1: Node, list2: Node) -> Node:
    i = 0
    j = 0
    l3l = Node()

    if list1 is None:
        return list2.copy()
    if list2 is None:
        return list1.copy()

    cur = l3l

    while list1 != None and list2 != None and list1.data != None and list2.data != None:
        if list1.data <= list2.data:
            if cur.data == None:
                cur.data = list1.data
            else:
                cur.next = Node(list1.data)
                cur = cur.next
            list1 = list1.next
            if list1 == None:
                break
        elif list2.data <= list1.data:
            if cur.data == None:
                cur.data = list2.data
            else:
                cur.next = Node(list2.data)
                cur = cur.next

            list2 = list2.next
            if list2 == None:
                break
    
    while list1 != None and list1.data != None:
        if cur.data == None:
            cur.data = list1.data
        else:
            cur.next = Node(list1.data)
            cur = cur.next
        list1 = list1.next
    while list2 != None and list2.data != None:
        if cur.data == None:
            cur.data = list2.data
        else:
            cur.next = Node(list2.data)
            cur = cur.next
        list2 = list2.next
    
    return l3l

l1 = map(int, input().split())
l2 = map(int, input().split())

l1l = LinkedList()
l2l = LinkedList()

for el in l1:
    l1l.append(el)
for el in l2:
    l2l.append(el)

l3l = mergeTwoLists(None, l2l.head)
breakpoint()