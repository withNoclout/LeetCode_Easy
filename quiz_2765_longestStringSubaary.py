class Solution : 
    def alternatingSubarray( self , nums ) : 
        if len(nums) < 2 : 
            return -1 
        
        ans = -1 
        i = 0 
        j = 1 
        next_expected = 1 
        n  = len(nums) 

        while j < n : 
            if( next_expected == 1 and nums[j] - nums[j-1] != 1 ) or ( next_expected == 0 and nums[j] - nums[j-1] != -1 ) :
                i = j- 1 
                if nums[j] - nums[i] != 1 :
                    i +=1 
                    next_expected = 1 
            if (next_expected == 0 and nums[j] - nums[j-1] == -1) or (next_expected == 1 and nums[j] - nums[j-1] == 1):
                ans = max( ans , j -i +1 ) 
                next_expected = 0 if next_expected == 1 else 1 

            j += 1 

        return ans
