class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s :
            return 0
        max_len = 1 
        curr_len = 1 
        curr_char = s[0]

        for i in range( 1 , len(s )) : 
            if s[i] == curr_char : 
                curr_len += 1 
                max_len  = max( max_len , curr_len ) 
            else : 
                curr_char = s[i] 
                curr_len = 1 

        return max_len 
     
