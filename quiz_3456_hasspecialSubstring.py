class Solution(object):
    def hasSpecialSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n = len(s) 
        for i in range( n- k + 1 )  :
            substring = s[i : i + k ] 
            if len( set(substring ) ) == 1 : 
                char = substring[0]

                if i > 0 and s[i-1 ] == char :
                    continue 

                if i + k < n and s[i+k] == char : 
                    continue 

                return True 
            
        return False 

