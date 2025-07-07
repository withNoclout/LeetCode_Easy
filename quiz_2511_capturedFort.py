class Solution(object):
    def captureForts(self, forts):
        """
        :type forts: List[int]
        :rtype: int
        """
        max_captured = 0 
        n = len( forts ) 

        i = 0 

        while i < n :
            if forts[i] == 1 or forts[i] == -1 :
                j = i +1 
                while j < n and forts[j] == 0 : 
                    j += 1 
                
                if j < n and forts[j] == - forts[i] : 
                    max_captured = max( max_captured , j - i - 1 ) 

                i = j 

            else : 
                i += 1 

        return max_captured
