class Solution(object):
    def semiOrderedPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) 
        pos1 = nums.index(1) 
        posN = nums.index(n) 

        if pos1 == 0 and posN == n - 1 : 
            return 0 
        
        swaps = pos1 + ( n - 1 - posN ) 

        if pos1 > posN : 
            swaps -= 1 

        return swaps
