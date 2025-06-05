class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        top = 0 
        front = 0 
        side = 0 

        for i in range(n) : 
            max_row = 0 
            max_col  = 0 
            for j in range(n ):
                if grid[i][j] > 0 :
                    top += 1 
                max_row = max(max_row, grid[i][j])
                max_col = max(max_col, grid[j][i])
            front += max_row
            side += max_col
        return top + front + side
