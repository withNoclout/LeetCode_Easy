class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_height(node, is_left):
            height = 0
            while node:
                height += 1
                node = node.left if is_left else node.right
            return height

        if not root:
            return 0

        left_height = get_height(root, True)
        right_height = get_height(root, False)

        if left_height == right_height:
            return (1 << left_height) - 1  # 2^height - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
