class Solution(object):
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = str( 2 * n )  + str(3* n   ) 

        if len(s ) != 9 or '0' in s : 
            return False 
        
        return len(set(s)) == 0 
