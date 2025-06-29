class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors )
        max_dist  = 0 

        for i in range( n )  : 
            for j in range( i+ 1 , n ) :
                if colors[i] != colors[j] :
                    max_dist = max(max_dist , abs(j - i ))

        return max_dist 
