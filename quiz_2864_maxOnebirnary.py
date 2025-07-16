class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        ones = s.count('1')
        n = len(s) 

        return '1'  * ( ones - 1 ) + '0' * ( n - ones ) + '1' 
