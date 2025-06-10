class Solution(object):
    def isBoomerang(self, points):
        """
        Check if three points form a boomerang (distinct and non-collinear).
        :type points: List[List[int]]
        :rtype: bool
        """
        # Extract points
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        
        # Check if points are distinct
        if (x1 == x2 and y1 == y2) or (x1 == x3 and y1 == y3) or (x2 == x3 and y2 == y3):
            return False
        
        # Check collinearity using cross-multiplication to compare slopes
        # (y2 - y1)/(x2 - x1) == (y3 - y1)/(x3 - x1)
        # => (y2 - y1)(x3 - x1) == (y3 - y1)(x2 - x1)
        return (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1)
