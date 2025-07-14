class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = max(nums) 
        if len( nums) != n +1 : 
            return False 
        
        count = {}
        for num in nums : 
            count[num ] = count.get(num , 0 ) + 1 

        for i in range( 1 , n ) :
            if count.get( i , 0 ) != 1 :
                return False 
        if count.get( n , 0 ) != 2 :
            return False 
        
        return True 
