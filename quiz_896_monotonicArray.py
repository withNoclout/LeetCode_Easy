class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        increasing = True 
        decreasing = True 

        for  i in range( len(nums)  - 1 ):
            if nums[i] > nums[i+1] : 
                increasing = False
            if nums[i] < nums[i+1] :
                decreasing = False
            if not increasing and not decreasing:
                return False    
            
        return True 
