class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        left_count = moves.count('L')
        right_count = moves.count('R')

        underscore_count = moves.count('_')

        return abs( right_count - left_count ) + underscore_count
