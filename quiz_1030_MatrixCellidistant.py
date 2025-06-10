class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        Return all cell coordinates sorted by Manhattan distance from (rCenter, cCenter).
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        result = []
        
        # Generate all possible coordinates
        for r in range(rows):
            for c in range(cols):
                result.append([r, c])
        
        # Sort by Manhattan distance
        result.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        
        return result
