class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums) 
        total = 0 

        for i in range(n) :
            is_good = True 
            if i - k >= 0 and nums[i] <= nums[i - k ] :
                is_good  = False 
            if i + k < n  and nums[i] <= nums[i+k ] :
                is_good =False 
            if is_good :
                total += nums[i]

        return total 
