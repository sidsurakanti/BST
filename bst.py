class BST:
	def __init__(self, value, left=None, right=None, parent=None):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent

	def search(self, target):
		"""
	    Search for a node in the binary search tree with the given value.

  		:param target: value to search for in the tree

  		:returns:
			<BST>: if node that contains target value is found
			NoneType: if node containing target value not found
	    """
		# target is not in the BST
		if self is None:
			return None
		# target found
		elif self.value == target:
			return self
		# search the right side of the tree
		elif self.value < target:
			return self.right.search(target) if self.right else None
		# search the left side of the tree
		else:
			return self.left.search(target) if self.left else None

	def height(self, tree) -> int:
		"""
  		Finds height of :param tree:
		
 		:param tree: 
  		"""
		if tree:
			# find height of left subtree recursively
			left_height = self.height(tree.left)
			# find height of right subtree recursively
			right_height = self.height(tree.right)
			return max(left_height, right_height) + 1
		return 0


# Sample binary tree for testing
root = BST(10)
root.left = BST(5, parent=root)
root.right = BST(15, parent=root)
root.left.left = BST(2, parent=root.left)
root.left.right = BST(7, parent=root.left)
root.right.left = BST(12, parent=root.right)
root.right.right = BST(20, parent=root.right)

target = root.search(20)
height = root.height(root)
print(target.value if target else None)
print(height)
