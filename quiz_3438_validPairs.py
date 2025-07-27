class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = [0] * 10 
        for digit in s : 
            freq[int(digit) ] += 1 

        for i in range(len(s) - 1 ) :
            d1, d2 = int( s[i] , int(s[i+1] ) ) 
            if d1 != d2 and freq[d1] == d1 and freq[d2 ] == d2 : 
                return s[i:i+2 ] 
            
        return "" 
