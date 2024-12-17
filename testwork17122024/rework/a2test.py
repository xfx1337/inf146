class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def mergeTwoLists(list1: Node, list2: Node) -> Node:
    i = 0
    j = 0
    l3l = Node()

    if list1 is None:
        #return list2
        list3 = Node(list2.data, list2.next)
        return list3
    if list2 is None:
        #return list1
        list3 = Node(list1.data, list1.next)
        return list3

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