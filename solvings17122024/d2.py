def swapPairs(head):
    if head and head.next:
        # Before: (head=c1) --> c2 --> c3
        #  After: (head=c2) --> c1 --> c3
        c1 = head
        c2 = c1.next
        c3 = c2.next
        head = c2
        c2.next = c1
        c1.next = c3
        cur = c1

        while cur.next and cur.next.next:
            # Before: cur --> c1 --> c2 --> c3
            #  After: cur --> c2 --> c1 --> c3
            c1 = cur.next
            c2 = c1.next
            c3 = c2.next
            cur.next = c2
            c2.next = c1
            c1.next = c3
            cur = c1

    return head