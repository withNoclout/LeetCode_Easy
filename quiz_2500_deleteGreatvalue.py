class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for row in grid :
            row.sort( reversed=True)

        answer = 0 

        for j in range( len( grid[0])) :
            max_val = 0 

            for i in range( len(grid)) :
                max_val = max( max_val , grid[i][j]) 
            answer += max_val 

        return answer 
