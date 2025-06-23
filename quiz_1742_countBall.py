class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        def digit_sum(n):
            return sum(int(digit) for digit in str(n))
        from collections import defaultdict

        box_counts = defaultdict(int)

        for ball in range( lowLimit, highLimit + 1):
            box_number = digit_sum(ball)
            box_counts[box_number] += 1 

        return max(box_counts.values()) if box_counts else 0
