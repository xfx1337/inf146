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

def mergeTwoLists(list1: Node, list2: Node) -> Node:
    l3l = LinkedList()
    i = 0
    j = 0
   
   # kostyly because i have already writen linkedlist class
    l1l = LinkedList()
    l2l = LinkedList()

    cur = list1
    while cur != None:
        l1l.append(cur.data)
        cur = cur.next
    cur = list2
    while cur != None:
        l2l.append(cur.data)
        cur = cur.next
    
    list1 = l1l
    list2 = l2l

    while i < list1.length and j < list2.length:
        if list1[i] < list2[j]:
            l3l.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            l3l.append(list2[j])
            j += 1
        else:
            l3l.append(list1[i])
            i += 1
            j += 1
    while i < list1.length:
        l3l.append(list1[i])
        i += 1
    while j < list2.length:
        l3l.append(list2[j])
        j += 1

    return l3l.head

l1 = map(int, input().split())
l2 = map(int, input().split())

l1l = LinkedList()
l2l = LinkedList()

for el in l1:
    l1l.append(el)
for el in l2:
    l2l.append(el)

l3l = mergeTwoLists(l1l.head, l2l.head)
breakpoint()