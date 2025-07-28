class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums)  : 
            digit_sum = sum( int(d ) for d in str(num  ) ) 

            if digit_sum == i :
                return i 
            
        return - 1
