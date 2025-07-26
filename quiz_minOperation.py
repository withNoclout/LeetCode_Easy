class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=  len(nums) 
        if len(set(nums)  ) == n :
            return 0 
        
        for k in range((n+2) // 3+ 1 ) :
            suffix = nums[3 * k :]

            if not suffix or len(set(suffix) ) == len(suffix ) :
                return k 
            
        return ( n+ 2 ) // 3 class Solution:
    def minOperations(self, grid ) : 
        m, n = len(grid), len(grid[0])
        ops = 0
        
        for j in range(n):  # Iterate over each column
            for i in range(1, m):  # Iterate down the rows for the column
                if grid[i][j] <= grid[i - 1][j]:
                    diff = grid[i - 1][j] - grid[i][j] + 1
                    ops += diff
                    grid[i][j] += diff  # Apply the operation directly
        return ops
