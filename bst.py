class BST:
	def __init__(self, value, left=None, right=None, parent=None):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent

def search(root: BST, target):
    """
    Binary search algorithm.
    """
    # target is not in the BST
    if root is None:
        return None
	# target found
    elif root.value == target:
        return root
	# search the right side of the tree
    elif root.value < target:
        return search(root.right, target)
	# search the left side of the tree
    else:
        return search(root.left, target)


# Sample binary tree for testing
root = BST(10)
root.left = BST(5, parent=root)
root.right = BST(15, parent=root)
root.left.left = BST(2, parent=root.left)
root.left.right = BST(7, parent=root.left)
root.right.left = BST(12, parent=root.right)
root.right.right = BST(20, parent=root.right)

target_node = search(root, 7)
