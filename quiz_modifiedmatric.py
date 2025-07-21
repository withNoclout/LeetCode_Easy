class Solution(object):
    def modifiedMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m ,  n = len( matrix  ) ,  len(matrix[0]  ) 
        answer = [ row[:] for row in matrix ] 
        col_maxs = [ max(col ) for col in zip(*matrix ) ] 

        for i in range(m) :
            for j in range(n) : 
                if answer[i][j] == -1 : 
                    answer[i][j] = col_maxs[j] 
        return answer 
