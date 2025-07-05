class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len( grid ) 

        maxLocal = [[0 ]* ( n-2 ) for _ in range(n-2 ) ] 

        for i in range( n- 2)  :
            for j in range( n- 2) :
                max_val = 0 

                for r in range(i , i+ 3 ) :
                    for c in range( j , j+3) :
                        max_val = max( max_val , grid[r][c] ) 

                maxLocal[i][j] = max_val 

        return maxLocal
