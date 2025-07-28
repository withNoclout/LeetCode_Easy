class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2 : 
            return 0 
        
        operations = 0 
        while True :
            is_sorted = True 
            for i in range( 1 , len(nums) ) :
                if nums[i] < nums[i-1 ] :
                    is_sorted = False 
                    break 
            if is_sorted : 
                break 

            min_sum = float('inf' ) 
            min_idx = 0 
            for i in range( len(nums ) - 1 ) :
                curr_sum = nums[i] + nums[i+1] 
                if curr_sum < min_sum : 
                    min_sum = curr_sum 
                    min_idx = i 

            nums[min_idx ] = nums[min_idx ] + nums[min_idx + 1 ] 
            nums.pop(min_idx+ 1 ) 
            operations += 1 

        return operations 
