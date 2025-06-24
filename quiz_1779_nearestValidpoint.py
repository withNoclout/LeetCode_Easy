class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        min_dist  = float('inf')
        index = -1 

        for i , ( px, py) in enumerate( points)  :
            if px == x or py == y :
                dist = abs( x- px ) + abs( y - py ) 
                if dist < min_dist :
                    min_dist = dist
                    index = i 

        return index 
