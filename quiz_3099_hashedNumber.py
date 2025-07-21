class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        digit_s = sum( int(d ) for d in str(x) ) 
        if x % digit_s == 0 :
            return digit_s 
        
        return - 1
