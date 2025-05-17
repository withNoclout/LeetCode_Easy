# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(nums) == 0:
            return None
        def sub(nums, i, j):
            if i > j:
                return None
            mid = (i + j) // 2
            cur = TreeNode( nums[mid]) 
            cur.left = sub(nums,i, mid - 1)
            cur.right = sub(nums,mid + 1, j)
            return cur

        return sub(nums, 0, len(nums) - 1)
