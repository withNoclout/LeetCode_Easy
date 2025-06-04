class Solution: 
    def dominantIndex( self , nums ) : 
        if not nums : 
            return -1 
        max_val = nums[0]
        max_index =  0 
        second_max = 0 

        for i in range( 1, len(nums  ) ) :
            if nums[i] > max_val :
                second_max = max_val 
                max_val = nums[i] 
                max_index = i  
            elif nums[i] > second_max : 
                second_max = nums[i] 

        if max_val >= 2 * second_max : 
            return max_index 
        return -1  
