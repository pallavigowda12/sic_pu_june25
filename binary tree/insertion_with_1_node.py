class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_node(root, value):
    new_node = TreeNode(value)
    if root is None:
        return new_node

    if root.left is None:
        root.left = new_node
    elif root.right is None:
        root.right = new_node

    return root

root = TreeNode(1)
insert_node(root, 2)


