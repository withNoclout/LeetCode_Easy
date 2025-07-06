class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) 

        for i in range( n-1 ) :
            if nums[i] == nums[i+1] :
                nums[i] *= 2 
                nums[i+1 ] = 0 

        result = [0] * n  
        pos = 0 
        for num in nums :
            if num != 0 :
                result[pop] = num 
                pos += 1 

        return result 
