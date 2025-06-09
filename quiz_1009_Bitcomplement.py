class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 : 
            return 1 
        
        k = 0 
        temp = n 
        while temp > 0 : 
            k += 1 
            temp //= 2 

        mask = ( 1 << k )  - 1 
        return mask ^ n  
