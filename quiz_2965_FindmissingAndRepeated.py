class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n =len(grid ) 
        n_sq = n * n 

        freq = [0] * ( n_sq + 1 ) 

        for i in range(n) : 
            for j in range(n)  : 
                freq[grid[i][j]] += 1 

        a = b =  0 

        for num in range( 1 , n_sq + 1 ) :
            if freq[num ] == 2  : 
                a = num 
            elif freq[num]  == 0 :
                b= num 

        return [a, b] 
