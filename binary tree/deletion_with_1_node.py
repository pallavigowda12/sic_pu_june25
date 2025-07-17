class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def delete_node(root, key):
    if root is None:
        return None
    if root.val == key:
        return None  # Delete the only node
    return root
