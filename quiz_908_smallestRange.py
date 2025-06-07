class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums : 
            return 0 
        max_val = max(nums)
        min_val = min(nums)

        return max( 0 ,  max_val - min_val - 2 * k )
