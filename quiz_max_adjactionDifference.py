class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) 
        max_diff = 0 
        for i in range( n )   : 
            diff = abs(nums[i] - nums[( i+ 1 ) % n ]   ) 

            max_diff = max( max_diff , diff)
        return max_diff
