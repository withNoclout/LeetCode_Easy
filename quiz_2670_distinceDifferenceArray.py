class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) 

        diff = [0] * n 

        for i in range(n)  :
            prefix = len(set(nums[:i+1]))
            suffix = len(set (nums[i+1: ]))
            diff[i] = prefix + suffix  
        return diff 
