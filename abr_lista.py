class NodeLista:
    def __init__(self, key):
        self.key = key
        self.duplicates = []
        self.left = None
        self.right = None

class ABRLista:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = NodeLista(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key == node.key:
            
            node.duplicates.append(NodeLista(key))
        elif key < node.key:
            if node.left is None:
                node.left = NodeLista(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = NodeLista(key)
            else:
                self._insert_recursive(node.right, key)