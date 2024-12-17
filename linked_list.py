class LL:
    def __init__(self):
        self.head = Unit()
  
    def __getitem__(self, key):
        i = 0
        current_node = self.head
        while i < key:
            if current_node.link != None:
                current_node = current_node.link
                i += 1
            else:
                raise ValueError("no such index in list")
        return current_node.value
    
    def __setitem__(self, key, value):
        i = 0
        current_node = self.head
        while i < key:
            if current_node.link != None:
                current_node = current_node.link
                i += 1
            else:
                raise ValueError("no such index in list")
        current_node.value = value

    def add(self, value):
        i = 0
        current_node = self.head
        while True:
            if current_node.link != None:
                current_node = current_node.link
                i += 1
            else:
                break
        unit = Unit(value)
        current_node.link = unit
    
    def remove(self, key):
        i = 0
        current_node = self.head
        while i < key-1:
            if current_node.link != None:
                current_node = current_node.link
                i += 1
            else:
                raise ValueError("no such index in list")
        if current_node != self.head or key == 1:
            to_del_node = current_node.link
            after_del = None
            if to_del_node != None:
                after_del = to_del_node.link
            current_node.link = after_del
            del to_del_node
    
    def insert(self, key, value):
        if key == 0:
            new_head = Unit(value)
            new_head.link = self.head
            self.head = new_head
            return
        i = 0
        prev_node = self.head
        while i < key-1:
            if prev_node.link != None:
                prev_node = prev_node.link
                i += 1
            else:
                raise ValueError("no such index in list")
        next_node = prev_node.link
        unit = Unit(value)
        prev_node.link = unit
        unit.link = next_node

    def l_length(self):
        i = 1
        current_node = self.head
        while True:
            if current_node.link != None:
                current_node = current_node.link
                i += 1
            else:
                break
        return i

    def __str__(self):
        a = ""
        for i in range(self.l_length()):
            a += (str(self[i]) + " ")
        return a

class Unit:
    def __init__(self, v=None, l=None):
        self.value = v
        self.link = l

x = LL()

inp = float(input())
x[0] = inp
while inp != "":
    a = input()
    try:
        a = float(a)
    except:
        break
    i = 0
    t = False
    while i < x.l_length():
        b = x[i]
        if b <= a:
            x.insert(i, a)
            t = True
            break
        i += 1
    if not t:
        x.add(a)
print(x)