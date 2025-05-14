class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        a, b = 1, 2  # base cases: 1 way to climb 1 step, 2 ways for 2 steps

        for i in range(3, n + 1):
            a, b = b, a + b

        return b
