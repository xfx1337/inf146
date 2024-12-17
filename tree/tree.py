class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

class Tree:
    def __init__(self):
        self.root = Node()

    def insert(self, key):
        pass
    
    def delete(self, key):
        pass
    
    def search(self, key):
        current = self.root
        path = "root"
        while current.value != key:
            if current.value == None:
                break
            if key > current.value:
                current = current.right
                path += "1"
            else:
                current = current.left
                path += "0"
        
        return path

# t = Tree()
# t.root.value = 4
# t.root.left = Node()
# t.root.left.value = 2
# t.root.left.left = Node()
# t.root.left.left.value = 1
# t.root.left.right = Node()
# t.root.left.right.value = 3
# t.root.right = Node()
# t.root.right.value = 10
# t.root.right.left = Node()
# t.root.right.left.value = 6
# t.root.right.right = Node()
# t.root.right.right.value = 123

print(t.search(123))