class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seq_sum = nums[0] 

        i = 1 

        while i < len(nums )  and nums[i] == nums[i-1 ] + 1 : 
            seq_sum += nums[i] 
            i += 1 

        num_set = set(nums) 

        x = seq_sum 

        while x in num_set : 
            x += 1 

        return x 
