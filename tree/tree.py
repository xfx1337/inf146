import random as rnd

class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

class Tree:
    def __init__(self):
        self.root = Node()

    def insert(self, key):
        if self.root.value == None:
            self.root.value = key
            return

        cur = self.root
        last = self.root
        direction = None
        while cur != None:
            last = cur
            if key >= cur.value:
                cur = cur.right
                direction = True
            else:
                cur = cur.left
                direction = False
        
        if direction:
            last.right = Node(key)
        else:
            last.left = Node(key)
    
    def delete(self, key):
        pass
    
    def search(self, key):
        current = self.root
        path = "root"
        while current != None:
            if current.value == None:
                return None
            if key > current.value:
                current = current.right
                path += "1"
            elif key < current.value:
                current = current.left
                path += "0"
            else:
                return path
        else:
            return None

t = Tree()
a = set()
for i in range(10):
    a.add(rnd.randint(0,10))

a = list(a)
rnd.shuffle(a)

for el in a:
    t.insert(el)

print(a)
x = input("search: ")
while x != "-1":
    print(t.search(int(x)))
    x = input("search: ")