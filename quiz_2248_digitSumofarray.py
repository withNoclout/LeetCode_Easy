class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        result = set(nums[0])

        for arr in nums[1:] : 
            result &= set(arr) 

        return sorted(list(result))
