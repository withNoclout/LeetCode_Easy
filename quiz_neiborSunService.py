class NeighborSum(object):

    def __init__(self, grid):
        """
        :type grid: List[List[int]]
        """
        self.grid = grid
        self.n = len(grid)

        self.value_to_pos = {}

        for i  in range(self.n) : 
            for j in range( self.n)  :
                self.value_to_pos[grid[i][j]] = (i, j)


    def adjacentSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        row , col = self.value_to_pos[value]
        total = 0 
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr ,dc in directions:
            r, c = row + dr , col +dc 
            if 0 <= r < self.n and 0 <= c < self.n : 
                total += self.grid[r][c] 
        return total 

    def diagonalSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        row , col = self.value_to_pos[value]
        total = 0 

        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr ,dc in directions:
            r, c = row+ dr , col +dc 
            if 0 <= r < self.n and 0 <= c < self.n : 
                total += self.grid[r][c]
        return total 


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
