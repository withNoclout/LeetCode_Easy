class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m ,n = len(matrix), len(matrix[0]) 
        result = [ [0] * m for _ in range(n) ]

        for i in range(m) :
            for j in range(n) :
                result[j][i] == matrix[i][j]

        return result
    

    error = "SyntaxError: invalid syntax"
