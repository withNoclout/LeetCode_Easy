class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x_coords = sorted( x for x  , y in points ) 

        max_width = 0 
        for i in range( 1 , len(x_coords )) :
            width = x_coords[i] - x_coords[i-1]
            max_width = max( max_width , width ) 

        return max_width 
