class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_gap = 0 
        prev_one = -1 
        pos = 0 

        while n >  0 : 
            if n & 1 : 
                if prev_one != -1 : 
                    max_gap = max( max_gap , pos - prev_one )
                prev_one = pos 
            n >>= 1 
            pos +=1  
        return max_gap 
    
        
