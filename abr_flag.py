class NodeFlag:
    def __init__(self, key):
        self.key = key
        self.has_duplicate = False 
        self.left = None
        self.right = None

class ABRFlag:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = NodeFlag(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key == node.key:
            
            node.has_duplicate = True
        elif key < node.key:
            if node.left is None:
                node.left = NodeFlag(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = NodeFlag(key)
            else:
                self._insert_recursive(node.right, key)