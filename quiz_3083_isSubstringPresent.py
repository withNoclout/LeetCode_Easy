class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        r_v = s[::-1 ] 

        for i in range( len(s) - 1 ) :
            sunstring = s[i:i+2 ] 
            if sunstring in r_v :
                return True 
        return False 
