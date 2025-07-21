class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums  ) 

        min_length = float('inf ' ) 

        for i in range(n)  :
            curr_or = 0 
            for j in range( i , n ) :
                curr_or |= nums[j] 
                if curr_or >=  k : 
                    min_length = min( min_length , j -i  + 1 ) 
                    break 


        return min_length if min_length != float('inf' ) else - 1 
