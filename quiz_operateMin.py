class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0 
        for num in nums : 
            if num < k  :
                count += 1 
        return count 
