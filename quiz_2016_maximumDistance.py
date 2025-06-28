class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_diff = -1 
        min_element = nums[0]

        for i in range(1 , len(nums)) :
            if nums[i] > min_element : 
                max_diff = max( max_diff , nums[i] - min_element ) 

            min_element = min( min_element , nums[i] )

        return max_diff
