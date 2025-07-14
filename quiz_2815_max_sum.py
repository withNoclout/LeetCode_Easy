class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_max_digit( num ) :
            return max( int(d) for d in str(num ) ) 
        
        max_sum = -1 
        n = len(nums) 

        for i in range(n) :
            for j in range( i+ 1 , n ) :
                if get_max_digit( nums[i]) == get_max_digit(nums[j] ) :
                    max_sum = max( max_sum , nums[i] + nums[j] ) 

        return max_sum
