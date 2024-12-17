class Node:
   def __init__(self, data, next=None):
       self.data = data
       self.next = None

def hasCycle(head):
    if head == None:
        return False
    cur_check = head
    while cur_check.next != None:
        cur = cur_check
        while cur.next != None:
            if cur.next == cur_check:
                return True
            cur = cur.next
        cur_check = cur_check.next
    return False