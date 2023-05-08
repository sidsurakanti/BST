class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def search(root: Node, target):
  """
  Binary-search algorithm
  """
  if root is None:
    return None
  elif root.value < target:
    return search(root.right, target)
  else:
    return search(root.left, target)
    
  return root

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)


search(root, 7)