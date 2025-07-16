class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums ) 
        collected = set()

        for i in range( n - 1,  -1 , -1  ) :
            if nums[i] <= k : 
                collected.append(nums[i] ) 
            if len(collected) == k : 
                return n  - i 
            
        return n 
