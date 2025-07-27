class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [ 0 if num % 2 == 0 else 1 for num in nums ] 

        nums.sort()
        return nums 
