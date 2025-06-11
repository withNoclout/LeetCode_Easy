class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1 :
            return "" 
        
        def gcd( a ,b ) :
            while b : 
                a ,b = b , a % b 
            return a 
        
        gcd_len = gcd( len( str1 ) , len(str2 ) ) 

        x = str1[:gcd_len ]

        return x 
    
