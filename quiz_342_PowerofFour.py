class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Must be > 0, and a power of 2 (only one bit set),
        # AND that bit must be in an even position (0-based)
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0
