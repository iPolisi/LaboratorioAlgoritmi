class NodeNormale:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class ABRNormale:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = NodeNormale(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = NodeNormale(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            
            if node.right is None:
                node.right = NodeNormale(key)
            else:
                self._insert_recursive(node.right, key)