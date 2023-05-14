A binary search tree

#### Functionality
- [x] `.search()`
- [x] `.inorder`
- [x] `.preorder`
- [x] `.min()`
- [x] `.__str__()`
- [x] `.__repr__()`
- [x] `.__getitem__()`
- [ ] `.insert()`
- [ ] `.remove()`

#### Usage
```md
BST
        10
       /  \
      5    15
     / \   / \
    2   7 12  20
```
```py
# create example binary tree
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
```
```hs
Height: 3
Inorder Traversal: [2, 5, 7, 10, 12, 15, 20]
Preorder Traversal: [10, 5, 2, 7, 15, 12, 20]
Is empty: False
Min value: 2
2, 5, 7, 10, 12, 15, 20
BST([2, 5, 7])
```

