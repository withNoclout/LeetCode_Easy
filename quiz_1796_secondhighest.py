class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = { int(ch) for ch in s if ch.isdigit()}

        if len(digits ) < 2 : 
            return -1 
        
        digits = sorted( digits, reverse=True ) 

        return digits[1]
