class BST:
	def __init__(self, value, left=None, right=None, parent=None):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent
    
	def height(self, tree) -> int:
		"""
  		Finds height of :param tree:
		
 		:param tree: <BST>
   		:returns: int
  		"""
		if tree:
			# find height of left subtree recursively
			left_height = self.height(tree.left)
			# find height of right subtree recursively
			right_height = self.height(tree.right)
			return max(left_height, right_height) + 1
		return 0

	@property
	def inorder(self):
		def traverse(node, res):
			if node:
				# traverse left subtree
				traverse(node.left, res)
				# append middle node value
				res.append(node.value)
				# traverse right subtree
				traverse(node.right, res)

		res = []
		traverse(self, res)
		return res
	
	@property
	def preorder(self):
		def traverse(node, res):
			if node:
				res.append(node.value)
				traverse(node.left, res)
				traverse(node.right, res)
				return

		res = []
		traverse(self, res)
		return res

	def min(self):
		"""
  		Returns minimum value in the BST

  		:returns: <BST>
  		"""
		cur = self
		# stop iterating if at the end of the BST
		while cur.left is not None:
			cur = cur.left
		# return last element searched
		return cur

	@property
	def is_empty(self):
		"""
  		Checks if tree is empty

  		:returns: bool
  		"""
		return False if self.right and self.left else True

	def _search(self, target):
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
			return self.right._search(target) if self.right else None
		# search the left side of the tree
		else:
			return self.left._search(target) if self.left else None
	
	def __getitem__(self, value):
		"""
  		Enables object indexing. BST[i]

  		:params value: value to search for in BST
		  :returns: 
  			<BST>: Node containing target value
  		"""
		return repr(self._search(value))

	def __str__(self):
		return ", ".join([str(n) for n in self.inorder])
	
	def __repr__(self):
		return f"BST({self.inorder})"


# Sample binary tree for testing
root = BST(10)
root.left = BST(5, parent=root)
root.right = BST(15, parent=root)
root.left.left = BST(2, parent=root.left)
root.left.right = BST(7, parent=root.left)
root.right.left = BST(12, parent=root.right)
root.right.right = BST(20, parent=root.right)

height = root.height(root)
inorder = root.inorder
preorder = root.preorder
empty = root.is_empty
min_val = root.min().value

print(f"Height: {height}")
print(f"Inorder Traversal: {inorder}")
print(f"Preorder Traversal: {preorder}")
print(f"Is empty: {empty}")
print(f"Min value: {min_val}")
print(root)
print(root[5])
