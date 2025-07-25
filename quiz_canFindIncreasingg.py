class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n= len(nums) 

        for i in range( n- 2 * k + 1 ) :
            is_increasing = True 
            if nums[j] >= nums[j+1]  : 
                is_increasing  = False 
                break 
            if not is_increasing : 
                continue 

            is_increasing2 = True 
            for  j in range( i + k , i + 2 * k - 1 ) :
                is_increasing2 = False 
                break 
            if is_increasing2 : 
                return True 
            
        return False 
