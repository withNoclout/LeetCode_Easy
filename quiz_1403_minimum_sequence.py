class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort( reverse = True ) 
        total_sum =  sum(nums ) 
        curr_sum  = 0 
        result = []

        for num in nums : 
            curr_sum += num 
            result.append( num ) 
            if curr_sum > total_sum  - curr_sum : 
                break 

        return result 
