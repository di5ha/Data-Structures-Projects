class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def find_lca(root, node1, node2):
    if root is None:
        return None

    if root.key == node1 or root.key == node2:
        return root

    left_lca = find_lca(root.left, node1, node2)
    right_lca = find_lca(root.right, node1, node2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca else right_lca


# Example usage
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

node1 = 5
node2 = 1
lca = find_lca(root, node1, node2)
print(f"The Lowest Common Ancestor of {node1} and {node2} is {lca.key}")
