class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if len(original) != m* n : 
            return [] 
        
        result = [] 

        for i in range( 0 , len(original ) , n) : 
            result.append( original[i:i+ n ] )

        return result 
