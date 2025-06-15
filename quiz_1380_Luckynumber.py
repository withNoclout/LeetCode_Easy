class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m , n = len( matrix )  , len(matrix[0] ) 
        lucky = [] 

        for i in range( m ) : 
            row_min = min( matrix[i])
            col_idx  = matrix[i].index(row_min ) 
            is_col_max = False 
            break 

        if is_col_max : 
            lucky.append( row_min ) 

        return lucky 
