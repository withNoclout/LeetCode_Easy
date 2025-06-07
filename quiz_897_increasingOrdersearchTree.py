# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        dummy = TreeNode(0)
        self.current = dummy
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.current.right = TreeNode(node.val)
            self.current = self.current.right
            inorder(node.right)

        inorder(root)
        return dummy.right  
