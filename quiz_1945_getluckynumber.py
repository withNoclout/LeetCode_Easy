class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        num = ''.join(str(ord(c) - ord('a') + 1) for c in s)
        for _ in range(k)  : 
            num = sum( int(digit ) for digit in str(num))

        return num 
