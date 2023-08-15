class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Inorder Traversal (Left-Root-Right)
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)

# Preorder Traversal (Root-Left-Right)
def preorder_traversal(root):
    if root:
        print(root.key, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Postorder Traversal (Left-Right-Root)
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.key, end=" ")


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Inorder Traversal:")
inorder_traversal(root)
print()

print("Preorder Traversal:")
preorder_traversal(root)
print()

print("Postorder Traversal:")
postorder_traversal(root)
print()
