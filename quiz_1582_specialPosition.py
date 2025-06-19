class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m , n = len(mat)  , len(mat[0])

        row_sum =  [ sum(row) for row in mat]
        col_sum =  [ sum(col  ) for col in zip(*mat)]

        count = 0 
        for i in range(m)  :
            for j in range(n) : 
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1  : 
                    count += 1 
        return count 
