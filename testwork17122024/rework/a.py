class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def mergeTwoLists(list1: Node, list2: Node) -> Node:
    i = 0
    j = 0
    l3l = Node()

    cur = l3l

    while list1 != None and list2 != None and list1.data != None and list2.data != None:
        if list1.data <= list2.data:
            cur.next = Node(list1.data)
            cur = cur.next
            list1 = list1.next
            if list1 == None:
                break
        elif list2.data <= list1.data:
            cur.next = Node(list2.data)
            cur = cur.next
            list2 = list2.next
            if list2 == None:
                break
    
    while list1 != None and list1.data != None:
        cur.next = Node(list1.data)
        cur = cur.next
        list1 = list1.next
    while list2 != None and list2.data != None:
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

l3l = mergeTwoLists(l1l.head, l2l.head)
breakpoint()