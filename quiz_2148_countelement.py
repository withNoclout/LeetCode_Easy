class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3 : 
            return 0 
        
        min_val = min(nums) 
        max_val = max(nums ) 


        count = sum( 1 for num in nums if min_val < num < max_val ) 

        return count 
