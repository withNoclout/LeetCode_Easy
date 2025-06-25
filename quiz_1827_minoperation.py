class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1 : 
            return 0 
        
        operations = 0 

        for i in range(1 , len(nums ) ) :
            if nums[i] <= nums[i-1 ] :
                increment = nums[i-1 ] - nums[i] + 1 
                operations += increment 
                nums[i] += increment 

        return operations 
