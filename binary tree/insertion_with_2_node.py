class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_node(root, value):
    new_node = TreeNode(value)
    if root is None:
        return new_node

    queue = [root]
    front = 0

    while front < len(queue):
        current = queue[front]
        front += 1

        if current.left is None:
            current.left = new_node
            break
        else:
            queue.append(current.left)

        if current.right is None:
            current.right = new_node
            break
        else:
            queue.append(current.right)

    return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
insert_node(root, 4)


