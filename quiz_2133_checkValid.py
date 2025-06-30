class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix  )
        for row in matrix : 
            if set(row ) != set(range( 1, n+1 ) ) :
                return False 
            
        for j in range(n) : 
            column = [ matrix[i][j] for i in range(n) ] 
            if set(column ) != set( range( 1, n+1 ) ) :
                return False 
            
        return True 
