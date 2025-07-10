class Solution(object):
    def findTheLongestBalancedSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0 
        i  = 0
        while i < len(s) : 
            zero_count = one_count = 0 

            while i < len(s) and s[i] == '0' : 
                zero_count += 1 
                i += 1 

            while i < len(s) and s[i] =='1' : 
                one_count += 1 
                i += 1 

            max_len = max( max_len , 2 * min(zero_count , one_count ) ) 

        return max_len 
