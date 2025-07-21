class Solution(object):
    def maxOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2  :
            return 0 
        score  = nums[0] + nums[1] 
        count = 1 
        for i in range( 2 , len(nums) - 1 , 2 ) :
            if nums[i] + nums[i+1 ] != score : 
                break 

            count += 1 
        return count 
