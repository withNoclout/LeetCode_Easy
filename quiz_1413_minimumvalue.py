class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_prefix_sum = 0  
        current_sum = 0 

        for num in nums : 
            current_sum += num 
            min_prefix_sum  = min( min_prefix_sum , current_sum ) 

        return max( 1 , 1- min_prefix_sum)
