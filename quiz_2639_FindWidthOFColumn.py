class Solution(object):
    def findColumnWidth(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m , n = len(grid )  , len(grid[0])

        ans  = [0] * n  

        for j in range(n)  : 
            max_len = 0 
            for i in range( m)  : 
                num = grid[i][j]
                length = len(str( abs(num)))  if num >= 0  else len(str(abs(num ))) +  1
                max_len  = max(max_len , length )

            ans[j] = max_len 

        return ans
