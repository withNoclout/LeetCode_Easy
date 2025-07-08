class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = str(n) 
        total = 0 

        for i in range( len( digits) ) :
            digit = int( digits[i])

            total += digit if i % 2 == 0 else -digit 

        return total 
