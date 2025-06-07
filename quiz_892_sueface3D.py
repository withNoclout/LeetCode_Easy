class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len( grid )

        total = 0 

        for i in range(n ) :
            for j in range(n ) : 
                if grid[i][j] == 0 :
                    continue
            v= grid[i][j] 
            total += 2 + 4 * v 
            total += 4 * v 
            if i > 0 :
                total -= min( v , grid[i-1][j] )
            if i < n- 1 : 
                total -= min( v , grid[i+1][j] )
            if j > 0 : 
                total -=  min( v , grid[i][j-1] )
            if j < n-1 : 
                total -=  min( v , grid[i][j+1] )
        return total 
