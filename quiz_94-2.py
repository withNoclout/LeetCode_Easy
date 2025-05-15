class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(values):
    if not values:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root

def inorderTraversal(root):
    result = []

    def dfs(node):
        if node:
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

    dfs(root)
    return result

# Build the tree from the list
root = buildTree([1, None, 2, 3])

# Perform in-order traversal
print(inorderTraversal(root))  # Output: [1, 3, 2]

