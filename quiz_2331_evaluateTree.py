# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root.left and not root.right : 
            return root.val == 1 
        
        left_result = evaluateTree( root.left)
        right_result = evaluateTree( root.right )

        if root.val == 2 : 
            return left_result or right_result 
        else : 
            return left_result and right_result
