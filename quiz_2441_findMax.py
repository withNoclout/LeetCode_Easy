class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums) 
        max_k = -1 

        for num in nums :
            if num > 0 and -num in num_set :
                max_k = max( max_k , num ) 

        return max_k 
