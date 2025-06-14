class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        col = n - 1
        
        for row in range(m):
            while col >= 0 and grid[row][col] < 0:
                col -= 1
            count += n - (col + 1)  # Count negatives in this row
            
        return count
