class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0 : 
            x = x * -1
        result = x ** 0.5 
                 
        return int(result) 
