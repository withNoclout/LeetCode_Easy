class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3 : 
            return -1 
        
        min_val = min(nums) 
        max_val = max(nums) 

        for num in nums :
            if num != min_val and num != max_val : 
                return num 
            
        return -1 
