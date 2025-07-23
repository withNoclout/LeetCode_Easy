class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums) 
        single_digit_sum = sum( num for num in nums if num < 10 ) 
        double_digit_sum  = sum( num for num in nums if 10 <= num <= 99 )  

        if single_digit_sum > total - single_digit_sum :
            return True 
        
        if double_digit_sum > total - double_digit_sum : 
            return True 
        
        return False 
