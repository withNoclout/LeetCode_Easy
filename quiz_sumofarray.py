class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0 
        for i in range( len(nums) ) :
            start = max(0 , i - nums[i] )
            total += sum(nums[start: i+ 1] )

        return total 
