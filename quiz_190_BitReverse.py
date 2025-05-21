class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(32):
            # Shift result to the left to make room for the next bit
            result = (result << 1) | (n & 1)
            # Shift input to the right to move to the next bit
            n >>= 1
        return result
