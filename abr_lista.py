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

    def get_altezza(self):
        return self._get_altezza_recursive(self.root)

    def _get_altezza_recursive(self, node):
        if node is None:
            return 0
        
        altezza_sinistra = self._get_altezza_recursive(node.left)
        altezza_destra = self._get_altezza_recursive(node.right)
        
        return 1 + max(altezza_sinistra, altezza_destra)            