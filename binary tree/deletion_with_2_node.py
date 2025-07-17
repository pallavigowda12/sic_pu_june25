class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def delete_deepest(root, d_node):
    queue = [root]
    front = 0
    while front < len(queue):
        current = queue[front]
        front += 1
        if current.left:
            if current.left == d_node:
                current.left = None
                return
            queue.append(current.left)
        if current.right:
            if current.right == d_node:
                current.right = None
                return
            queue.append(current.right)

def delete_node(root, key):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return None if root.val == key else root

    queue = [root]
    front = 0
    key_node = None
    last_node = None

    while front < len(queue):
        current = queue[front]
        front += 1
        if current.val == key:
            key_node = current
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        last_node = current

    if key_node:
        key_node.val = last_node.val
        delete_deepest(root, last_node)

    return root
