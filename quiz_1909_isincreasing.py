class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len( nums ) 
        def is_increasing( arr ) :
            for i in range(1 , len(arr) ) :
                if arr[i] <= arr[i-1] : 
                    return False 
            return True 
        
        if is_increasing( nums ) : 
            return True 
        
        for i in range(n) : 
            temp = nums[:i] + nums[i+1 : ] 
            if is_increasing(temp ) : 
                return True 
            
        return False 
