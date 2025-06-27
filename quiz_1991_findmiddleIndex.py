class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums ) 
        left_sum = 0 

        for i in range(len(nums )) :
            right_sum = total_sum - nums[i] - left_sum 

            if left_sum == right_sum : 
                return i 
            
            left_sum += nums[i] 

        return -1 
