class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def invert_binary_tree(root):
    if root is None:
        return
    else:
        invert_binary_tree(root.left)
        invert_binary_tree(root.right)
        root.left, root.right = root.right, root.left
    return root
