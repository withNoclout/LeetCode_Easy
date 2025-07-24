class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digit_sum(num ) :
            total = 0 
            while num > 0  : 
                total += num % 10
                num //= 10
            return total 
        
        tranformed=  [ digit_sum(num) for num in nums ] 

        return min(tranformed)
