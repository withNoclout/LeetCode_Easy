class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        lower = set()
        upper = set()

        for c in s :
            if c.islower() :
                lower.add(c) 
            else : 
                upper.add(c)

        for c in range( 90 , 64 , -1 ) :
            if chr(c).lower() in lower and chr(c) in upper : 
                return chr(c) 
            
        return ""
