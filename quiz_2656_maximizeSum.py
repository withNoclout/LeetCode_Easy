class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_num = max(nums) 
        total = max_num 
        for i in range( 1, k ) :
            max_num += 1 
            total += max_num 

        return total 
