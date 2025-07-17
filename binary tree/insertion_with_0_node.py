class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_node(root, value):
    new_node = TreeNode(value)
    if root is None:
        return new_node  # Create root node
    return root


root = None
root = insert_node(root, 1)


