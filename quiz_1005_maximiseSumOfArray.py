class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort() 
        i =  0 

        while i < len(nums ) and k > 0 and nums[i] < 0  : 
            nums[i] =  - nums[i] 

            k-=1 
            i += 1 

        if k > 0 :
            min_idx = i - 1 if i > 0 else 0 
            if i < len(nums) and nums[i] < nums[min_indx] :
                min_idx = i

            if k % 2 == 1 :
                nums[min_idx] = -nums[min_idx]
        return sum(nums)
    

# ERROR 
