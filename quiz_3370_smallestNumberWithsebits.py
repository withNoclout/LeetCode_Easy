class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        x= n 
        while bin(x).count('1' ) != bin(x).bit_length():
            x += 1
        return x
    
