class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = list(s) 

        def shift( c , x )  :
            return chr( ord(c) + x ) 
        
        for i in range( 1 , len( s) ,  2 ) : 
            result[i] = shift(s[i-1]  , int(s[i]))

        return ''.join(result)
